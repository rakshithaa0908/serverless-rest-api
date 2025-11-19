# Deployment Steps – Lambda + API Gateway + DynamoDB

## 1. Create DynamoDB Table
1. Open AWS Console → DynamoDB  
2. Click **Create table**
3. Enter:
   - Table name: `registration-form`
   - Partition key: `email` (String)
4. Click **Create table**
5. (Optional) Add items manually:
   - Open table
   - Select **Explore table items**
   - Click **Create item**

---

## 2. Create IAM Role for Lambda
1. Open **IAM Console**
2. Click **Roles → Create role**
3. Trusted entity type: **AWS Service**
4. Select **Lambda**
5. Click **Next**
6. Attach policies:
   - `AmazonDynamoDBFullAccess`
   - `AWSLambdaBasicExecutionRole`
7. Click **Next**
8. Role name: `microrole`
9. Click **Create role**

---

## 3. Create Lambda Function
1. Open **Lambda Console**
2. Click **Create function**
3. Enter:
   - Name: `registration-form-function`
   - Runtime: Python 3.12+
   - Execution role: Select existing role → `microrole`
4. Click **Create function**
5. Replace the default code with your `lambda_function.py` file
6. Click **Deploy**
7. Test with:

```json
{
  "httpMethod": "POST",
  "body": "{\"email\":\"test@example.com\", \"first_name\":\"John\", \"last_name\":\"Doe\", \"address\":\"Test\", \"phno\":\"9999\"}"
}

---

## 4. Create REST API in API Gateway
1. Open **API Gateway**
2. Click **Create API**
3. Select **REST API → Build**
4. API type: **New API**
5. Name: `registration-api`
6. Click **Create API**

---

## 5. Create Resource and POST Method
1. In Resources → Click **Create Resource**
2. Resource name: `register`
3. Click **Create Resource**
4. Select `/register` → Click **Create Method**
5. Method: **POST**
6. Enable **Lambda Proxy Integration**
7. Integration type: **Lambda Function**
8. Select your function: `registration-form-function`
9. Click **Save**

---

## 6. Enable CORS
1. Select `/register`
2. Click **Enable CORS**
3. Choose **POST**
4. Save changes

---

## 7. Deploy API
1. Click **Actions → Deploy API**
2. Stage: **New Stage**
3. Name: `proddeploy`
4. Click **Deploy**
5. Copy the Invoke URL

---

## 8. Update Frontend
Paste the Invoke URL in `api.js` as:

```javascript
const API_URL = "https://your-api-id.execute-api.ap-south-1.amazonaws.com/proddeploy/register";
```
---

## 9. Test
1. Open your HTML registration form in the browser
2. Enter first name, last name, address, email and phone number
3. Click **Submit**
4. Check DynamoDB:
   - Open DynamoDB
   - Select table `registration-form`
   - Click **Explore table items**
5. Confirm that the new user record is stored successfully

---