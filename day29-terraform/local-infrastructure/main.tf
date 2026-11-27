resource "local_file" "cloud_support_info" {
  filename = "${path.module}/cloud-support-info.txt"

  file_permission      = "0644"
  directory_permission = "0755"

  content = <<-EOT
    Project: AI Cloud Support Assistant
    Environment: Local Terraform Lab
    Day: 29
    Tool: Terraform
    Purpose: Infrastructure as Code and change-detection practice
  EOT
}

