import boto3
from .base_tagger import AwsResourceTagger
from utils.id_formatter import extract_resource_name

# Concrete class for tagging Ec2 Unencrypted Snapshots
class Ec2UnencryptedSnapshotTagger(AwsResourceTagger):
    def add_tags(self):
        print(f"Tagging Ec2 Unencrypted Snapshot: {self.resource_arn} in region {self.region}")
        resource_id = extract_resource_name(self.resource_arn)
        ec2 = boto3.client('ec2', region_name=self.region)
        try:
            ec2.create_tags(Resources=[resource_id], Tags=self.tags)
        except Exception as e:
            print(f"Error tagging Ec2 Unencrypted Snapshot {self.resource_arn}: {e}")