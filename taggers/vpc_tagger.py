import boto3
from .base_tagger import AwsResourceTagger

# Concrete class for tagging VPCs
class VPCTagger(AwsResourceTagger):
    def add_tags(self):
        print(f"Tagging VPC: {self.resource_id} in region {self.region}")
        ec2 = boto3.client('ec2', region_name=self.region)
        try:
            ec2.create_tags(Resources=[self.resource_id], Tags=self.tags)
        except Exception as e:
            print(f"Error tagging VPC {self.resource_id}: {e}")