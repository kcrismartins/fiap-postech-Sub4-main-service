provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "sales_service_vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_vpc" "main_service_vpc" {
  cidr_block = "10.1.0.0/16"
}

resource "aws_db_instance" "sales_service_db" {
  allocated_storage    = 20
  engine               = "postgres"
  engine_version       = "13.4"
  instance_class       = "db.t3.micro"
  name                 = "sales_service"
  username             = "admin"
  password             = "password123"
  vpc_security_group_ids = [aws_security_group.sales_service_sg.id]
}

resource "aws_db_instance" "main_service_db" {
  allocated_storage    = 20
  engine               = "postgres"
  engine_version       = "13.4"
  instance_class       = "db.t3.micro"
  name                 = "main_service"
  username             = "admin"
  password             = "password123"
  vpc_security_group_ids = [aws_security_group.main_service_sg.id]
}
