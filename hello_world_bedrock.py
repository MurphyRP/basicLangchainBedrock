"""
Hello World application using LangChain with Amazon Bedrock inference profile.
This simple script demonstrates how to set up and use Amazon Bedrock
with LangChain for text generation using a cross-region inference profile.
"""
import os
import json
import logging
from langchain_aws.chat_models import ChatBedrock

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_bedrock_credentials(credentials_file='config.json'):
    """
    Load Amazon Bedrock credentials from a file.
    
    Args:
        credentials_file (str): Path to the credentials file
        
    Returns:
        dict: Credentials as a dictionary
    """
    try:
        with open(credentials_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading credentials: {e}")
        print(f"Make sure the {credentials_file} file exists and contains valid JSON.")
        exit(1)

def run_hello_world_with_inference_profile(inference_profile_id, region_name):
    """
    Run a hello world example using a Bedrock inference profile.
    
    Args:
        inference_profile_id: The ID of the inference profile to use
        region_name: AWS region name
    """
    try:
        # Set up the ChatBedrock model with the inference profile ID
        print(f"Initializing ChatBedrock with inference profile: {inference_profile_id}")
        
        # Model parameters for the specific model
        model_kwargs = {
            "temperature": 0.7,
            "max_tokens": 500
        }
        
        # Initialize ChatBedrock with the inference profile ID
        chat_model = ChatBedrock(
            model_id=inference_profile_id,
            region_name=region_name,
            model_kwargs=model_kwargs
        )
        
        # Create a prompt
        prompt = "What's the meaning of 'Hello World' in programming?"
        
        print("Sending request to Amazon Bedrock using inference profile...")
        try:
            # Invoke the model
            response = chat_model.invoke(prompt)
            
            print("\n--- Response from Amazon Bedrock ---")
            print(response.content)
            print("-----------------------------------\n")
        except Exception as e:
            print("\n--- ERROR ---")
            print(f"Failed to get response from Bedrock: {str(e)}")
            print(f"Error type: {type(e).__name__}")
            print("------------\n")
        
        print("Hello World demonstration complete!")
    
    except Exception as e:
        print("\n--- ERROR ---")
        print(f"Failed to initialize Bedrock: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        print("------------\n")

def main():
    # Load credentials
    print("Loading Amazon Bedrock credentials...")
    credentials = load_bedrock_credentials()
    
    # Set up AWS credentials from our loaded file
    os.environ["AWS_ACCESS_KEY_ID"] = credentials.get("aws_access_key_id")
    os.environ["AWS_SECRET_ACCESS_KEY"] = credentials.get("aws_secret_access_key")
    
    # Specify the region based on the inference profile
    aws_region = "us-east-2"  # Region for our inference profile
    
    # Inference profile ID
    inference_profile_id = "us.meta.llama3-1-8b-instruct-v1:0"
    
    # Run the example with the inference profile
    run_hello_world_with_inference_profile(inference_profile_id, aws_region)

if __name__ == "__main__":
    main()