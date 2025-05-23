This project captures the process of deploying a containerised Flask application on AWS using the Continous Integration, Continous Deployment (CI/CD) culture. this aligns with DevOps principles. Thus, every code change we make will automatically reflect through the GitHub actions.

### Key Features, Tools and Services
1. Python (Flask framework)
2. GitHub and GitHub Actions
3. Docker
4. AWS services
5. Terraform

With Terraform as the IAC tool, the first step is to write our code for deploying the various AWS services needed for the app. The AWS services include:

1. EC2 Instance
2. VPC
3. ECR (Elastic Container Registry)
4. Subnets and Routetables
5. Security Groups

The terraform files are contained in this repository, they include files that end with ".tf"
In order to use terraform to deploy, we run:

    terraform init
    terraform plan
    terraform apply

The above initialises our terraform files, then it displays the various services we are trying to deploy. the "terraform apply" finally launces these services into our AWS Management console.
