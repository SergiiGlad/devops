
Download the exiting project IAM policy:
```
gcloud projects get-iam-policy ${PROJECT_ID} > policy.yaml
```


Role Name | Permissions
--- | ---

roles/viewer | Permissions for read-only actions that do not affect state, such as viewing (but not modifying) existing resources or data.

roles/editor | All viewer permissions, plus permissions for actions that modify state, such as changing existing resources.

roles/owner | All editor permissions and permissions for the following actions:

Manage roles and permissions for a project and all resources within the project.
Set up billing for a project.

roles/browser |Read access to browse the hierarchy for a project, including the folder, organization, and Cloud IAM policy. This role doesn't include permission to view resources in the project.