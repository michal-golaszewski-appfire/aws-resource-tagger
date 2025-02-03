import boto3
from .base_tagger import AwsResourceTagger

# Concrete class for tagging AppRunner AutoScaling Configurations
class EcrPrivateRepositoryTagger(AwsResourceTagger):
    def add_tags(self):
        print(f"ECR Repository: {self.full_resource_id} in region {self.region}")
        apprunner = boto3.client('ecr', region_name=self.region)
        try:
            apprunner.tag_resource(resourceArn=self.full_resource_id, tags=self.tags)
        except Exception as e:
            print(f"Error tagging ECR Repository {self.full_resource_id}: {e}")