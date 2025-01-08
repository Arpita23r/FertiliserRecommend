# 🌾 Fertilizer Recommendation API 🌟

Welcome to the **Fertilizer Recommendation API**! This API uses machine learning to recommend the best fertilizer for your crops based on input parameters like temperature, humidity, soil type, and crop type. 🚜✨  

Access the API:  
🌐 **Hosted URL**: [https://fertiliserrecommend.onrender.com](https://fertiliserrecommend.onrender.com)  
📑 **API Documentation**: [https://fertiliserrecommend.onrender.com/docs](https://fertiliserrecommend.onrender.com/docs)  

---

## 🚀 Features  
- **Custom Fertilizer Recommendation**: Get the most suitable fertilizer for your crops.  
- **Flexible Input**: Accepts multiple crop and soil types with detailed parameters.  
- **Interactive Documentation**: Explore and test API endpoints directly through the provided Swagger docs.  

---

## 🗂 File Structure  

```
├── images/                 # Placeholder for any images used
├── templates/              # Templates for rendering views (if needed)
├── Procfile                # Deployment configuration
├── app.py                  # Main application logic
├── f2.csv                  # Supporting CSV file (sample data)
├── fertilizer_model.pkl    # Trained ML model
├── label_encoders.pkl      # Label encoders for categorical data
├── requirements.txt        # Python dependencies
```

---

## 🧪 Input Parameters  

The API requires the following inputs:  
1. **Temperature**: (float)  
2. **Humidity**: (float)  
3. **Moisture**: (float)  
4. **Soil_Type**: (string)  
5. **Crop_Type**: (string)  
6. **Nitrogen**: (int)  
7. **Potassium**: (int)  
8. **Phosphorous**: (int)  

---

## 🌍 Unique Soil Types  
The API recognizes the following soil types, ensuring accurate fertilizer recommendations:  

- **Clayey**  
- **Loamy**  
- **Black**  
- **Sandy**  
- **Red**  

Each soil type has unique properties that impact fertilizer selection for optimal crop yield.  

---

## 🔧 How to Use  

1. Clone the repository:  
   ```bash
   git clone https://github.com/Arpita23r/FertiliserRecommend.git
   cd FertiliserRecommend
   ```  

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

3. Run the application locally:  
   ```bash
   uvicorn app:app --reload
   ```  

4. Visit `http://127.0.0.1:8000/docs` to interact with the API locally.  

---

## 🖼 Example Request  

### Endpoint: `/recommend`  
**Method**: `POST`  
**Input** (JSON):  
```json
{
  "Temperature": 28.5,
  "Humidity": 60.0,
  "Moisture": 30.0,
  "Soil_Type": "Loamy",
  "Crop_Type": "Paddy",
  "Nitrogen": 10,
  "Potassium": 15,
  "Phosphorous": 8
}
```  

**Response**:  
```json
{
  "Recommended Fertilizer": "Urea"
}
```  

---

## ✨ Deployed API  

Check out the hosted API and its documentation:  
- 🌐 **[API URL](https://fertiliserrecommend.onrender.com)**  
- 📑 **[Documentation](https://fertiliserrecommend.onrender.com/docs)**  

---

## 🤝 Contributing  

Contributions are always welcome! Feel free to submit a pull request or open an issue for suggestions and improvements.  

---

## 📫 Contact  

For any questions or feedback, please contact the repository owner through GitHub or raise an issue.  

Enjoy farming smarter! 🌱✨  

---
