# Deployment

## Prerequisites

- Salesforce org with API access
- One Salesforce Integration user licence
- Salesforce API Integration permission set licence
- n8n instance with Data Tables
- Gemini API credential

## Salesforce identity

Create a dedicated user:

| Setting | Value |
| --- | --- |
| User licence | Salesforce Integration |
| Profile | Minimum Access – API Only Integrations |
| Role | None |
| Active | Yes |

Assign the Salesforce API Integration permission set licence.

Create a permission set with no user-licence restriction:

```text
VANTIX Governance Metadata Read Access
```

Enable:

- API Enabled
- View Setup and Configuration
- View Roles and Role Hierarchy when Salesforce adds it as a dependency

Do not enable Manage Flow, Customize Application, View All Data, Modify All Data, Author Apex, or metadata modification permissions.

## External Client App

Configure:

| Setting | Value |
| --- | --- |
| Distribution | Local |
| OAuth scope | Manage user data via APIs |
| Flow | Client Credentials |
| Permitted users | Admin approved users are pre-authorized |
| Run As | Dedicated integration user |
| Selected permission sets | VANTIX Governance Metadata Read Access only |

Do not select a System Administrator profile. Do not include refresh-token scope.

## n8n credentials

Create an OAuth2 API credential:

| Field | Value |
| --- | --- |
| Grant type | Client Credentials |
| Token URL | `https://YOUR_MY_DOMAIN.my.salesforce.com/services/oauth2/token` |
| Client authentication | Body |
| Scope | Blank |

Store Consumer Key and Consumer Secret only in the credential.

Create the Gemini credential separately.

## History table

Create `dpmo_scan_history` with:

| Column | Suggested type |
| --- | --- |
| runid | String |
| scandate | String or Date/Time |
| dpmo | Number |
| sigmalevel | Number |
| totalDefects | Number |
| totalOpportunities | Number |

After import, reselect this table in both Data Table nodes.

## Import checklist

1. Import `workflows/Salesforce-Governance-Sentinel-v1.3-public.json`.
2. Replace `YOUR_MY_DOMAIN`.
3. Select the Salesforce credential in both Salesforce HTTP Request nodes.
4. Select the Gemini credential in both Gemini nodes.
5. Select `dpmo_scan_history` in both Data Table nodes.
6. Confirm no node contains pinned data.
7. Execute the isolated Salesforce test node.
8. Verify `totalSize`, `done`, and customer-owned records.
9. Execute the complete workflow.
10. Confirm schema status `PASSED` and download the report.

## Production hardening

Before commercial production, add:

- fixed outbound IP and Salesforce IP restrictions;
- a schedule or authenticated webhook trigger;
- encrypted external persistence and retention policy;
- pagination;
- centralized logging and alerting;
- tenant isolation;
- secret rotation;
- backup and disaster recovery;
- data-processing agreement and privacy notice;
- role-based report access;
- automated deletion and evidence-retention controls.

