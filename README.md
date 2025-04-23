# AWS Bedrock Hello World

A simple example demonstrating how to use AWS Bedrock with LangChain and cross-region inference profiles.

## Overview

This project provides a minimal example of how to use AWS Bedrock LLM service with the LangChain framework. It demonstrates:

- Setting up AWS credentials
- Initializing a ChatBedrock model using an inference profile
- Sending a simple query to the model
- Processing the response

## Prerequisites

- Python 3.9 or higher
- AWS account with access to Amazon Bedrock
- AWS IAM user with Bedrock permissions
- Access granted to the foundation models you want to use

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/aws-bedrock-hello-world.git
cd aws-bedrock-hello-world
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

Activate the virtual environment:

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your AWS credentials
- [ ] Rename `sample_config.json` to `config.json`
- [ ] Edit `config.json` to add your AWS access key and secret key:

```json
{
  "aws_access_key_id": "YOUR_ACCESS_KEY_ID",
  "aws_secret_access_key": "YOUR_SECRET_ACCESS_KEY"
}
```

### 5. Request access to models
- [ ] Go to AWS Bedrock console
- [ ] Navigate to "Model access"
- [ ] Request access to the models you need

## Running the Example

To run the Hello World example:

```bash
python hello_world_bedrock.py
```

The script will:
1. Load your AWS credentials from `config.json`
2. Initialize a ChatBedrock model with an inference profile
3. Send a simple prompt to the model
4. Display the response

## Customizing

You can modify the script to use different models or inference profiles:

| Parameter | Description | Example |
| --- | --- | --- |
| `inference_profile_id` | The ID of the inference profile to use | `"us.meta.llama3-1-8b-instruct-v1:0"` |
| `model_kwargs` | Parameters for model generation | `{"temperature": 0.7, "max_tokens": 500}` |
| `region_name` | AWS region for the model | `"us-east-2"` |

Example code modification:

```python
# Change the inference profile
inference_profile_id = "us.anthropic.claude-3-sonnet-20240229-v1:0"

# Adjust model parameters
model_kwargs = {
    "temperature": 0.5,  # Lower temperature for more deterministic responses
    "max_tokens": 1000   # Increase token limit for longer responses
}
```

## Troubleshooting

### Common Issues

- **Access Denied Error**
  - Ensure your IAM user has the correct permissions for Bedrock
  - Check your AWS credentials in `config.json`

- **Model Not Found**
  - Verify you've been granted access to the model in the Bedrock console
  - Check the inference profile ID is correct

- **Invalid Parameters**
  - Check the [model documentation](https://docs.aws.amazon.com/bedrock/) for supported parameters
  - Different models support different parameters

## Resources

- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [LangChain Documentation](https://python.langchain.com/docs/)
- [LangChain AWS Integration](https://python.langchain.com/docs/integrations/providers/aws/)

## License

[MIT](LICENSE)