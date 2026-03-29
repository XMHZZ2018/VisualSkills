# aws-iam-roles-policies

Configure custom AWS IAM roles and policies in the AWS Console, then attach them to roles and users.

## Usage

```
/aws-iam-roles-policies
```

## Workflow

### Step 1: Navigate to IAM

1. Sign in to the **AWS Management Console**
2. In the top search bar, search for **IAM** and open **Identity and Access Management (IAM)**
3. You will see the IAM dashboard with the left sidebar containing: Dashboard, User groups, Users, Roles, Policies, Identity providers, Account settings

### Step 2: Create a Custom IAM Role

1. In the left sidebar, click **Roles**
2. Click the **Create role** button (top right)
3. On the **Select trusted entity** page (Step 1):
   - Choose the trusted entity type. Options include:
     - **AWS service** — for allowing AWS services like EC2, Lambda, or S3 to perform actions
     - **AWS account** — for cross-account access
     - **Web identity** — for federated users via external identity providers
     - **SAML 2.0 federation** — for corporate directory federation
     - **Custom trust policy** — for writing a custom trust policy JSON
   - Select **AWS service**
   - In the service search box, type the service name (e.g., `S3`)
   - Select the service (e.g., **S3**) and choose a use case
   - Click **Next**
4. On the **Add permissions** page (Step 2):
   - You can skip adding permissions for now (we will create and attach a custom policy later)
   - Click **Next**
5. On the **Name, review, and create** page (Step 3):
   - **Role name**: Enter a descriptive name (e.g., `allow-s3-access`)
   - **Description**: Enter a description (e.g., `Allows S3 to call AWS services on your behalf.`)
   - Review the **Trust policy** JSON which will look like:
     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Principal": {
             "Service": "s3.amazonaws.com"
           },
           "Action": "sts:AssumeRole"
         }
       ]
     }
     ```
   - Click **Create role**
6. You will see a green banner: **Role `allow-s3-access` created.**

### Step 3: Create a Custom IAM Policy

1. In the left sidebar, click **Policies**
2. Click **Create policy**
3. On the **Specify permissions** page (Step 1):
   - Toggle the **Policy editor** to **JSON** mode (click the JSON tab)
   - Enter a custom policy document. For example, to allow all S3 actions on all resources:
     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Sid": "AllowS3Access",
           "Effect": "Allow",
           "Action": "s3:*",
           "Resource": "*"
         }
       ]
     }
     ```
   - **Important**: Ensure valid JSON syntax — the console will show a red error icon and "Fix all syntax errors to view this panel" if there are issues
   - Once S3 appears under **Included** in the service filter, the policy is valid
   - Click **Next**
4. On the **Review and create** page (Step 2):
   - **Policy name**: Enter a meaningful name (e.g., `custom-s3-allow`)
   - **Description** (optional): Describe the policy purpose
   - Review the **Permissions defined in this policy** section
   - Click **Create policy**
5. You will see a green banner: **Policy `custom-s3-allow` created.**

### Step 4: Attach the Custom Policy to the Role

1. In the left sidebar, click **Roles**
2. Search for and click on the role you created (e.g., `allow-s3-access`)
3. On the role details page, go to the **Permissions** tab
4. Click the **Add permissions** dropdown button
5. Select **Attach policies**
6. Search for your custom policy (e.g., `custom-s3-allow`)
7. Select the checkbox next to the policy and click **Add permissions**
8. You will see a green banner: **Policy was successfully attached to role.**
9. The policy now appears under **Permissions policies** with:
   - **Policy name**: `custom-s3-allow`
   - **Type**: Customer managed
   - You can expand it to see the full JSON policy document

### Step 5: Attach the Custom Policy to a User

1. In the left sidebar, click **Users**
2. Click on the target user (e.g., `test-user-demo`)
3. On the user details page, go to the **Permissions** tab
4. Click the **Add permissions** dropdown button
5. Choose the permissions option:
   - **Add user to group** — recommended approach for managing permissions via groups
   - **Copy permissions** — copy from another user
   - **Attach policies directly** — attach a managed policy directly to the user
6. Select **Attach policies directly**
7. Search for your custom policy (e.g., `custom-s3-allow`)
8. Select the checkbox and click **Next**, then **Add permissions**
9. You will see a green banner: **1 policy added**
10. The policy appears in the user's permissions list as **Customer managed**, attached **Directly**

### Step 6: Verify Access

1. Sign in as the user who received the policy (or test with the role)
2. Navigate to the relevant AWS service (e.g., **S3**)
3. Verify that the user can now perform the allowed actions (e.g., list and access S3 buckets)
4. If access is denied, check:
   - The policy is correctly attached to the user/role
   - The policy JSON has the correct `Action` and `Resource` values
   - There are no conflicting deny policies

## Notes

- **Principle of least privilege**: Use specific actions (e.g., `s3:GetObject`, `s3:ListBucket`) instead of wildcards (`s3:*`) in production
- **Resource scope**: Use specific ARNs (e.g., `arn:aws:s3:::my-bucket/*`) instead of `"Resource": "*"` to limit access
- **Customer managed vs AWS managed**: Custom policies show as "Customer managed" in the Type column; AWS-provided policies show as "AWS managed"
- **Attach up to 10 managed policies** per role
- **Maximum session duration** for roles defaults to 1 hour
- **Policy name constraints**: Max 128 characters, alphanumeric plus `+=,.@-_`
- **Role name constraints**: Max 64 characters, alphanumeric plus `+=,.@-_`
- Prefer attaching policies to **groups** rather than individual users for easier management at scale
- Use **IAM Access Advisor** (tab on role/user details) to audit which services have been accessed
