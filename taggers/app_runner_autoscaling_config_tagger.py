import boto3
from .base_tagger import AwsResourceTagger
from utils.adapt_tag_sets import adapt_tags

# Concrete class for tagging AppRunner AutoScaling Configurations
class AppRunnerAutoscalingConfigTagger(AwsResourceTagger):
    def add_tags(self):
        self.tags = adapt_tags(self.tags) 
        print(f"AppRunner Autoscaling Configuration: {self.full_resource_id} in region {self.region}")
        apprunner = boto3.client('apprunner', region_name=self.region)
        try:
            apprunner.tag_resource(resourceArn=self.full_resource_id, tags=self.tags)
        except Exception as e:
            print(f"Error tagging CloudWatch Log Group {self.resource_id}: {e}")