---
name: libreoffice_calc-knowledge-multimodal-v1
description: "Practical with-screenshots guides for LibreOffice Calc 7.3.7. Consult via the load_topic MCP tool — it returns the guide text and every figure in one atomic call."
---

# LibreOffice Calc 7.3.7 Knowledge (multimodal-v1)

## How to consult this skill

This skill exposes two MCP tools (already registered for you):

- **`load_topic(topic)`** — returns the chosen topic's `guide.md` AND every figure (PNG) in that topic folder as one tool response. **Use this instead of `Read` for any `*.md` or `figXX.png` inside this skill.**
- **`list_topics()`** — returns every topic path available, one per line.

Each entry in the TOC below has the form `[Title](<topic>/guide.md)`. The `<topic>` part (the path before `/guide.md`) is what you pass to `load_topic`.

> You will receive the guide text plus the relevant figures in a single tool result — no extra `Read` calls needed.

**Rules:**

1. Before any GUI action where you are unsure of the menu path / dialog / icon, find the matching topic in the TOC and call `load_topic` first.
2. You may call `load_topic` **at any step** of the trajectory, not only at the start. If the task moves into a new area, call `load_topic` again for the new area.
3. Do **not** issue separate `Read` calls for `figXX.png` files inside this skill — they are delivered by `load_topic` automatically.

## Guides

### Spreadsheet Fundamentals

- [Basic Formulas & Operations](spreadsheet-fundamentals/basic-formulas/guide.md) — Core spreadsheet functions including SUM, AVERAGE, VLOOKUP, conditional formatting, sorting, and chart creation
  - **Use when:** entering formulas with operators, relative and absolute cell references, SUM/PRODUCT functions, statistical functions (AVERAGE/MIN/MAX/MEDIAN), IF conditional formulas, using Function Wizard (Ctrl+F2)
- [Data Import, Export & Transformation](spreadsheet-fundamentals/data-import-export/guide.md) — Importing CSV files, reformatting data for external systems, pivoting data layouts, and comparing dataset versions
  - **Use when:** importing CSV or text files, saving as Excel or CSV, exporting as PDF, creating pivot tables, emailing spreadsheets as attachments, Text Import dialog settings
- [Spreadsheet Formatting & Layout](spreadsheet-fundamentals/spreadsheet-formatting/guide.md) — Document cleanup, print layout configuration, professional formatting with merged cells and borders, and window setup
  - **Use when:** merging and splitting cells, text wrapping and alignment, cell borders and background colors, AutoFormat styles, defining print ranges, page headers and footers
- [Weighted Grade Calculation](spreadsheet-fundamentals/weighted-calculation/guide.md) — Computing weighted averages for gradebooks, what-if grade scenarios, and required-score calculations
  - **Use when:** weighted grade calculation with SUMPRODUCT, percentage weight normalization, what-if scenario with Multiple Operations dialog, two-variable sensitivity table, Goal Seek for target grade, rounding weighted averages with ROUND

### Data Cleaning & Repair

- [Formula Debugging & Auditing](data-cleaning-and-repair/formula-debugging/guide.md) — Fixing circular references, #REF!/#NAME?/#VALUE! errors, broken SUM ranges, and auditing undocumented formula logic across sheets
  - **Use when:** tracing precedents and dependents, resolving formula error codes, using Detective tool, enabling Value Highlighting, fixing #DIV/0! with IF, auditing cross-sheet references
- [Data Standardization](data-cleaning-and-repair/data-standardization/guide.md) — Normalizing inconsistent date formats, standardizing field values, and cleaning messy records into uniform structure
  - **Use when:** data validation with Validity dialog, find and replace inconsistent values, mark invalid data with Detective, normalizing date formats, enabling regular expressions in formulas, sorting to surface outliers
- [Data Deduplication & Consolidation](data-cleaning-and-repair/data-deduplication/guide.md) — Merging scattered data sources, removing duplicate entries, and consolidating records into a clean unified dataset
  - **Use when:** removing duplicate rows, consolidating data from multiple sheets, Data Consolidate dialog, Standard Filter no duplications, AutoFilter toggle values, Advanced Filter with criteria range
- [Record Validation & Verification](data-cleaning-and-repair/record-validation/guide.md) — Checking records for logical consistency, flagging discrepancies, and verifying calculations against source data
  - **Use when:** setting up data validity criteria, creating input help and error alerts, marking invalid data with Detective, tracing formula precedents, resolving formula error codes, using value highlighting

### Financial Analysis

- [Cost Comparison & Best-Value Analysis](financial-analysis/cost-comparison/guide.md) — Comparing prices, plans, or quotes across multiple options to identify the most cost-effective choice
  - **Use when:** cost comparison formulas (SUM MIN MAX RANK), conditional formatting for best value, color scale formatting, named ranges via Define dialog, hiding and showing columns, IF function for price comparison
- [Expense Tracking & Budget Variance](financial-analysis/expense-tracking/guide.md) — Tracking spending, calculating cost-per-use, reconciling receipts, and analyzing budget overruns
  - **Use when:** expense tracking layout in Calc, SUMIF for category totals, budget variance formulas, conditional formatting for budget overruns, color scale heat map, budget vs actual column chart
- [Insurance Plan Comparison](financial-analysis/insurance-comparison/guide.md) — Evaluating health or auto insurance plans across usage scenarios including deductibles, premiums, and out-of-pocket costs
  - **Use when:** comparing insurance plans in Calc, using Data Multiple Operations tool, two-variable comparison grid, Goal Seek break-even analysis, XY Scatter chart for cost crossover, MIN RANK functions for plan ranking
- [Loan & Mortgage Analysis](financial-analysis/loan-analysis/guide.md) — Calculating loan payments, payoff strategies, risk scoring, and refinance break-even timelines
  - **Use when:** loan payment calculation with PMT, amortization with IPMT/PPMT/CUMIPMT, extra payment payoff with NPER, Goal Seek for loan amount or break-even, Solver for multi-loan optimization, Function Wizard for financial functions
- [Tax Deduction & Depreciation](financial-analysis/tax-deduction/guide.md) — Calculating mileage deductions, asset depreciation, and tax-related financial records
  - **Use when:** mileage deduction formulas, asset depreciation with DB/DDB functions, named ranges for tax sheets, rounding tax figures, cross-sheet references for quarterly totals, flagging deduction thresholds with IF
- [Transaction & Rewards Analysis](financial-analysis/transaction-analysis/guide.md) — Analyzing transaction histories, optimizing credit card rewards, and detecting anomalous transactions
  - **Use when:** AutoFilter for transactions, Standard Filter with AND/OR conditions, Advanced Filter with criteria range, sorting by multiple keys with natural sort, Find All for merchant lookup, Group and Outline for period subtotals
- [Fair Split & Settlement Calculation](financial-analysis/fair-split-calculation/guide.md) — Proportionally dividing shared costs, tips, rent, or settlement amounts among participants
  - **Use when:** splitting shared expenses, equal and proportional cost splitting, absolute cell references for dragging formulas, SUM COUNT ROUND IF functions, formatting cells as currency, settlement balance sanity check
- [Billing, Invoicing & Pricing](financial-analysis/billing-and-invoicing/guide.md) — Calculating billable amounts, reconciling invoices against statements, and developing pricing strategies
  - **Use when:** creating invoices from Calc templates, billing formulas for subtotals and tax, formatting cells as currency, saving spreadsheets as reusable templates, tracing formula errors with Detective, pricing analysis with statistical functions

### Health & Wellness

- [Medication Scheduling & Refills](health-and-wellness/medication-management/guide.md) — Calculating refill dates, validating drug interaction timing, and managing dosage schedules
  - **Use when:** tracking medication refill dates with date arithmetic, calculating days remaining with TODAY(), setting date validation via Data Validity dialog, adding input help tooltips for cells, configuring error alerts for invalid entries, formula-based custom validation for drug interaction timing
- [Fitness & Exercise Tracking](health-and-wellness/fitness-tracking/guide.md) — Analyzing workout logs for progressive overload and calculating running pace metrics
  - **Use when:** tracking workout sets reps weight, calculating running pace with time formatting, charting exercise progress with Line and Scatter charts, using Descriptive Statistics for training data, progressive overload analysis formulas, referencing non-adjacent data ranges in Chart Wizard
- [Sleep Quality Analysis](health-and-wellness/sleep-analysis/guide.md) — Analyzing sleep data for patterns, efficiency percentages, and correlations with lifestyle factors
  - **Use when:** sleep quality statistics with AVERAGE MEDIAN MIN MAX, correlation analysis via Data Statistics Correlation, linear regression via Data Statistics Regression, XY scatter charts with trend lines, moving average smoothing for weekly trends
- [Blood Donation Eligibility Tracking](health-and-wellness/blood-donation-tracking/guide.md) — Calculating next eligible donation dates based on donation type and waiting period rules
  - **Use when:** blood donation eligibility date formulas, cell date format settings, Data Validity dropdown lists, date validation with TODAY(), COUNTIF eligibility summaries, VLOOKUP reference table lookups
- [Health & Nutrition Monitoring](health-and-wellness/health-monitoring/guide.md) — Tracking vital signs, symptoms, hydration, feeding patterns, and macronutrient targets over time
  - **Use when:** tracking vitals and nutrition in spreadsheet, AVERAGE MIN MAX COUNT formulas, Descriptive Statistics dialog, Insert Chart Wizard line chart, stacked area percentage chart, XY Scatter plot setup

### Home & Property Management

- [Maintenance & Service Tracking](home-and-property/maintenance-tracking/guide.md) — Tracking service intervals, cumulative mileage, and overdue maintenance for vehicles, bikes, pools, and facilities
  - **Use when:** maintenance service interval tracking, data validity rules for cell input, conditional formatting with color scale and icon sets, managing conditional formatting rules, date acceptance patterns locale settings, value highlighting with Ctrl+F8
- [Renovation Material & Cost Estimation](home-and-property/renovation-estimation/guide.md) — Calculating material quantities, waste factors, costs, and project timelines for home renovation tasks
  - **Use when:** estimating renovation material costs with formulas, using absolute cell references for waste factors, summing and averaging project costs, flagging budget overruns with IF conditions, running what-if scenarios with Multiple Operations, tracking project timelines with date math
- [Home Inventory Management](home-and-property/inventory-management/guide.md) — Tracking household supplies, insurance inventories, and emergency preparedness items with expiration monitoring
  - **Use when:** tracking home inventory in Calc, defining named ranges, AutoFilter and Standard Filter for inventory, sorting inventory data, expiration date monitoring with formulas, managing multiple inventory sheets with database ranges
- [Utility & Energy Analysis](home-and-property/utility-analysis/guide.md) — Analyzing energy bills, meter readings, solar production, and water usage to detect anomalies and leaks
  - **Use when:** meter reading consumption tracking, anomaly detection with Descriptive Statistics, outlier flagging formulas, energy and solar trend charts, regression analysis for solar panel degradation, moving average smoothing for utility data
- [Appliance Lifecycle Management](home-and-property/appliance-management/guide.md) — Tracking appliance warranties, analyzing failure patterns, and making repair-vs-replace decisions
  - **Use when:** tracking appliance warranties with date formulas, conditional formatting for warranty status, color scale for repair costs, statistics functions for failure analysis, Goal Seek for repair-vs-replace breakeven, managing conditional formatting rules

### Scheduling & Coordination

- [Trip & Route Planning](scheduling-and-coordination/trip-planning/guide.md) — Building travel itineraries with distance, fuel, time, and elevation calculations for road trips and hikes
  - **Use when:** calculating trip distances and fuel consumption, using Fill Series for date itineraries, creating custom sort lists for route names, flagging route segments with IF formulas, defining named ranges for elevation data, computing cumulative distance totals
- [Event & Gathering Management](scheduling-and-coordination/event-management/guide.md) — Managing RSVPs, seating, auction bids, sign-up sheets, and logistics for parties, weddings, and community events
  - **Use when:** event RSVP tracking, defining named ranges for guest lists, multi-level sorting of seating charts, AutoFilter for auction bids, advanced filtering sign-up sheets, finding guests with Find toolbar
- [Schedule Conflict Detection](scheduling-and-coordination/schedule-conflict-detection/guide.md) — Identifying time overlaps, availability windows, and scheduling conflicts across participants or resources
  - **Use when:** detecting schedule overlaps, sorting by date and start time, using AutoFilter to filter by participant, Standard Filter for time conflicts, Advanced Filter with criteria range, COUNTIFS for overlap detection
- [Deadline & Renewal Tracking](scheduling-and-coordination/deadline-tracking/guide.md) — Calculating days remaining, urgency priority, and visual alerts for approaching deadlines and renewals
  - **Use when:** deadline countdown with TODAY(), days remaining formula, conditional formatting for deadlines, color scale and icon set formatting, date acceptance patterns configuration, managing conditional format rules
- [Group Fairness & Compliance](scheduling-and-coordination/group-compliance/guide.md) — Balancing shared duties, enforcing policies, tracking co-op credits, and ensuring equitable participation
  - **Use when:** using SUM AVERAGE MIN MAX for fairness checks, SUBTOTAL function with AutoFilter, Data Subtotals grouping by employee or category, collapsible outline for group totals, pre-sort and case-sensitive subtotal options
- [Lending & Borrowing Tracking](scheduling-and-coordination/lending-tracking/guide.md) — Tracking loaned items, calculating overdue fees, and investigating damage or missing returns
  - **Use when:** tracking loans and borrowing in Calc, defining named ranges for lending tables, setting up Data Validity dropdown lists, calculating overdue fees with date formulas, filtering with AutoFilter and Standard Filter, marking invalid data with Detective

### Lifestyle & Hobbies

- [Plant & Garden Care Tracking](lifestyle-and-hobbies/plant-and-garden-care/guide.md) — Managing watering schedules, propagation success rates, and seed viability for houseplants and gardens
  - **Use when:** tracking plant watering schedules, filling date series in Calc, using COUNTIF with wildcards, setting up cell validity dropdown lists, creating custom sort lists, expanding formula bar for multi-line input
- [Animal & Pet Care Tracking](lifestyle-and-hobbies/animal-care/guide.md) — Tracking pet vaccinations, veterinary medication inventory, aquarium water quality, and beekeeping inspections
  - **Use when:** tracking pet vaccination schedules, setting up cell validation dropdowns, defining named ranges for data tables, configuring date formats, inserting special characters, creating database ranges for medication inventory
- [Hobby & Activity Log Analysis](lifestyle-and-hobbies/hobby-log-analysis/guide.md) — Organizing and analyzing logs for reading, music practice, gaming, photography, collections, and outdoor activities
  - **Use when:** sorting activity logs by date, filtering with AutoFilter and Advanced Filter, summarizing with COUNT SUM AVERAGE COUNTIF, generating Descriptive Statistics report, creating and editing Pivot Tables, finding entries with Ctrl+F
- [Food & Beverage Tracking](lifestyle-and-hobbies/food-and-beverage/guide.md) — Tracking freshness, fermentation, expiration dates, and tasting notes for coffee, homebrew, wine, and perishables
  - **Use when:** tracking food expiration dates, formatting date and time cells, setting data validity rules with dropdown lists, sorting inventory by expiration, using COUNTIF with wildcards, enabling regular expressions in Calc formulas
- [Meal Planning & Recipe Scaling](lifestyle-and-hobbies/meal-and-recipe/guide.md) — Scaling recipes, consolidating shopping lists, planning meal rotations, and calculating ingredient quantities
  - **Use when:** scaling recipe servings with formulas, weekly meal planning grid, consolidated shopping list with SUM, Data Multiple Operations for what-if comparisons, named ranges for readability, IF formulas for budget alerts
- [Craft Material Calculation](lifestyle-and-hobbies/craft-calculation/guide.md) — Calculating fabric yardage, yarn quantities, and material costs for quilting and knitting projects
  - **Use when:** calculating craft material yardage, using SUM AVERAGE MAX for costs, IF formula for budget warnings, Data Multiple Operations for what-if scenarios, cross-sheet cell references, setting up labeled spreadsheet layout
- [Competition & League Scoring](lifestyle-and-hobbies/competition-scoring/guide.md) — Calculating standings, normalizing judge scores, and determining rankings for leagues and contests
  - **Use when:** ranking contestants with RANK, dropping highest and lowest scores, sorting standings by score, filtering by division with AutoFilter, SUBTOTAL for filtered results, normalizing judge scores

