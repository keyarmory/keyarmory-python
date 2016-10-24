## Key Armory client library for Python

This is the official Python client library for the Key Armory Encryption Key Orchestration Service. You'll first need an account by going to https://keyarmory.com. Follow the instructions to set up a project and key pool and then place the API Key you receive in the initialization script below.

### Installation
```
copy file into project
```

### Initialization
```python
keyarmory = KeyArmory({
    'api_key': 'your_api_key_here'
})
```

### Encryption
```python
ct_string = keyarmory.encrypt(your_data)
```

### Decryption
```python
your_data = keyarmory.decrypt(ct_string)
```