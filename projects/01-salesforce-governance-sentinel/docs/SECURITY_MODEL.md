# Security Model

## Identity chain

```text
n8n encrypted OAuth credential
→ VANTIX Governance Sentinel External Client App
→ Vantix Governance Scanner API-only user
→ VANTIX Governance Metadata Read Access permission set
→ Salesforce Flow setup metadata
```

## Salesforce configuration

| Layer | Configuration |
| --- | --- |
| User licence | Salesforce Integration |
| Profile | Minimum Access – API Only Integrations |
| Permission set licence | Salesforce API Integration |
| Permission set | VANTIX Governance Metadata Read Access |
| System permissions | API Enabled; View Setup and Configuration; Salesforce-required View Roles and Role Hierarchy dependency |
| External Client App | Local; API scope only |
| OAuth flow | Client Credentials |
| Permitted users | Admin approved users are pre-authorized |
| Run As | Dedicated Vantix Governance Scanner user |
| Authorized permission set | VANTIX Governance Metadata Read Access only |

## Data minimization

The query reads:

- Flow definition ID
- API name and label
- namespace
- active and latest version IDs
- process type
- description

It does not read Accounts, Contacts, Opportunities, Cases, users' business data, files, emails, or customer records.

## Credential handling

- Consumer Key and Secret are stored only in n8n Credentials.
- Gemini API key is stored only in n8n Credentials.
- Workflow exports contain credential references, not secret values.
- The public workflow removes local credential IDs and org-specific URLs.
- Generated reports contain run evidence but no authentication material.

## Revocation

Access can be stopped by any of these independent controls:

1. Deactivate the integration user.
2. Remove the permission-set assignment.
3. Remove the permission set from the External Client App.
4. Disable the External Client App.
5. Rotate or revoke the Consumer Secret.
6. Delete or disable the n8n credential.

## Residual risks

| Risk | Treatment |
| --- | --- |
| Cloud n8n lacks fixed outbound IP | Temporarily relax app IP restrictions; add fixed egress before production |
| Client Secret compromise | Rotate secret and review OAuth usage |
| AI overstates impact from labels | Keep deterministic severity inputs visible and require human approval |
| Large-org pagination | Add `nextRecordsUrl` loop before enterprise deployment |
| Metadata may reveal business process names | Minimize logs and restrict execution access |

