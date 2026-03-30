# MainStreet Media Skills

## Notion CRM

**Token:** ntn_b32176806275xYfW0hu14lLZBCasLlc2TZygz8WHt5V6A3

### Databases
- Leads: 3330bfc9e8f3806bae5cfa98186b328d
- Clients: 3330bfc9e8f3805ab5cec6667538585f
- Content Calendar: 3330bfc9e8f380fc898dfbc7b9fea22c
- Tasks: 3330bfc9e8f3801eb9e9d9076f42a5fa

### Usage
```bash
# Query leads
curl -s -X POST "https://api.notion.com/v1/databases/3330bfc9e8f3806bae5cfa98186b328d/query" \
  -H "Authorization: Bearer ntn_b32176806275xYfW0hu14lLZBCasLlc2TZygz8WHt5V6A3" \
  -H "Notion-Version: 2022-06-28" -d "{}"

# Add new lead/page
curl -s -X POST "https://api.notion.com/v1/pages" \
  -H "Authorization: Bearer ntn_b32176806275xYfW0hu14lLZBCasLlc2TZygz8WHt5V6A3" \
  -H "Notion-Version: 2022-06-28" \
  -d '{"parent": {"database_id": "LEADS_ID"}, "properties": {...}}'
```

### Properties by Database
**Leads:** Name, Deal stage, Deal value, Lead source, Email, Phone, Notes, Follow up Date, Priority level, Decision maker, Expected close date, Last contact date

**Clients:** Name, Business, Tier, Status (Onboarding/Active/At Risk/Churned), Monthly Posts, Monthly Revenue, Renewal Date, Contact Email, Notes

**Content Calendar:** Content name, Platform, Status (Idea/Drafting/Editing/Scheduled/Published), Content type, Film date, Publish date, Post URL, Owner, Client (relation)

**Tasks:** Task name, Description, Task type, Status, Priority, Due date, Assignee