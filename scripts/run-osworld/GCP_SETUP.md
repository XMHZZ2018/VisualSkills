# GCP VM Setup for OS World Evaluation

## 1. Create the VM

Create an N2 instance with nested virtualization enabled (required for Docker + KVM):

```bash
# Create a boot disk with nested virtualization
gcloud compute disks create osworld-disk \
    --zone=us-west1-b \
    --size=200GB \
    --type=pd-ssd \
    --image-family=debian-12 \
    --image-project=debian-cloud

# Create the VM with nested virtualization license
gcloud compute instances create osworld \
    --zone=us-west1-b \
    --machine-type=n2-standard-16 \
    --boot-disk-name=osworld-disk \
    --enable-nested-virtualization
```

Key specs:
- **Machine type**: `n2-standard-16` (16 vCPUs, 64GB RAM) — needed for KVM + Docker overhead
- **Disk**: 200GB SSD — OS World qcow2 image is ~20GB, plus Docker layers
- **Nested virtualization**: required for KVM inside Docker containers

## 2. SSH config

Add to `~/.ssh/config` on your local machine:

```
Host osworld
    HostName <EXTERNAL_IP>
    User <USERNAME>
    IdentityFile ~/.ssh/google_compute_engine
```

## 3. Install dependencies on the VM

```bash
ssh osworld

# Install system packages
sudo apt-get update
sudo apt-get install -y docker.io qemu-kvm python3-pip python3-venv git rsync

# Add user to docker and kvm groups
sudo usermod -aG docker $USER
sudo usermod -aG kvm $USER

# Re-login for group changes
exit
ssh osworld

# Verify KVM
ls /dev/kvm   # should exist

# Verify Docker
docker run hello-world
```

## 4. Install Claude CLI

```bash
# Install Claude CLI (Node.js required)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
npm install -g @anthropic-ai/claude-code

# Authenticate
claude login
```

## 5. Clone MMSkills and set up

```bash
git clone --recurse-submodules https://github.com/XMHZZ2018/MMSkills.git
cd MMSkills

# Create Python venv
python3 -m venv venv
source venv/bin/activate

# Install OSWorld + dependencies
bash scripts/run-osworld/setup.sh
```

## 6. Prepare the OS World Docker image

OS World uses a qcow2 disk image inside Docker containers with QEMU/KVM.

```bash
cd ~/MMSkills

# Download and extract the qcow2 image (one-time)
mkdir -p docker_vm_data
cd docker_vm_data

# Download from OSWorld's official source
wget https://drive.google.com/... -O osworld_image.zip   # see OSWorld README for URL
unzip osworld_image.zip
cd ..

# The docker_vm_data/ directory should contain the qcow2 image
# OSWorld's Docker provider looks for ./docker_vm_data/ relative to CWD
# run.py handles this with os.chdir(osworld_root)
```

Note: `docker_vm_data/` should be placed in the OSWorld root (`vendor/OSWorld/docker_vm_data/`) or symlinked there. The evaluation script changes to that directory before creating containers.

## 7. Run evaluation

```bash
cd ~/MMSkills
source venv/bin/activate

# Test with a single task
python3 scripts/run-osworld/run.py \
    --provider_name docker \
    --specific_task_id bb5e4c0d-f964-439c-97b6-bdb9747de3f4

# Run all Chrome tasks (background)
nohup python3 scripts/run-osworld/run.py \
    --provider_name docker \
    --domain chrome --skill_mode none \
    > ~/osworld_run.log 2>&1 &

# Monitor progress
tail -f ~/osworld_run.log
grep 'score=' ~/osworld_run.log
```

## 8. Sync results back to local

```bash
# From local machine
rsync -avz osworld:~/MMSkills/scripts/run-osworld/workspaces/ scripts/run-osworld/workspaces/
```

## Troubleshooting

### Disk full
```bash
# Check disk usage
df -h

# Resize disk (from local machine)
gcloud compute disks resize osworld-disk --zone=us-west1-b --size=300GB

# Expand filesystem (on VM)
sudo growpart /dev/sda 1
sudo resize2fs /dev/sda1
```

### KVM not available
```bash
# Verify nested virtualization is enabled
grep -c vmx /proc/cpuinfo   # should be > 0

# If 0, the VM was created without --enable-nested-virtualization
# Must recreate the VM with that flag
```

### Docker container stuck booting
```bash
# Check running containers
docker ps

# Kill stuck containers
docker kill $(docker ps -q)
docker rm $(docker ps -aq)
```

### growpart not found
```bash
sudo apt-get install cloud-guest-utils
```
