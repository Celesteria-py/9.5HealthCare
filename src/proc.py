
import google.generativeai as genai
import time

genai.configure(api_key="AIzaSyBDA_oPmEDITYfO8YOZSmpzXMum-Or-ZP0")

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
)


def getPrompt(text, type):
    prompt = ''

    if type == "bmi":
        prompt = f"""Bạn hãy cung cấp cho tôi chỉ số BMI và tôi sẽ mô tả vóc dáng tương ứng theo cấu trúc sau:
"[Mức BMI]: [Phân loại]"
Ví dụ:
"23.5: Bình thường"
{text}: [Phân loại]
"""

    if type == 'predict':
        prompt = f"""Người dùng đã cung cấp các thông tin sau về tình trạng sức khỏe của họ:

* **Cân nặng:** {text[0]}
* **Chiều cao:** {text[1]}

Dựa trên thông tin trên, hãy tính toán các chỉ số sau:

1. **Chỉ số BMI:**  Tính toán BMI của người dùng. 
2. **Mức độ cân nặng:** Xếp loại mức độ cân nặng của người dùng dựa trên chỉ số BMI (ví dụ:  thiếu cân, bình thường, thừa cân,...).  
3. **Rủi ro tiềm ẩn:**  Liệt kê một số vấn đề sức khỏe mà người dùng có **thể** gặp phải dựa trên BMI (nếu có). 

**Lưu ý:**

* Chỉ đưa ra thông tin về chỉ số BMI và phân loại mức độ cân nặng. Không đưa ra bất kỳ chẩn đoán hay lời khuyên y tế nào.
* Nhấn mạnh rằng thông tin này chỉ mang tính chất tham khảo. Khuyến khích người dùng tìm kiếm sự tư vấn từ chuyên gia y tế để được đánh giá chính xác tình trạng sức khỏe."""

    if type == 'analysis':
        prompt = f"""
        Người dùng đã cung cấp các thông tin sau về tình trạng sức khỏe của họ:

* **Cân nặng:** {text[0]}
* **Chiều cao:** {text[1]}
* **Tiền sử bệnh án:** {text[2]}
* **Triệu chứng hiện tại:** {text[3]}
* **Mức độ ảnh hưởng của triệu chứng:** {text[4]}
* **Biện pháp đã thực hiện để cải thiện:** {text[5]}
* **Vấn đề sức khỏe khác:** {text[6]}
* **Mong muốn nhận được hỗ trợ:** {text[7]}

Bạn hãy đóng vai trò là một chuyên gia sức khỏe, phân tích kỹ lưỡng các thông tin trên và đưa ra một bài phân tích chi tiết về tình trạng sức khỏe hiện tại của người dùng.  Bài phân tích cần bao gồm:

1. **Đánh giá tổng quan:**  Đánh giá chung về tình trạng sức khỏe dựa trên thông tin đã cho (ví dụ:  dưới mức trung bình, trung bình, khỏe mạnh). 
2. **Phân tích chi tiết:** Phân tích mối liên hệ giữa cân nặng, chiều cao, tiền sử bệnh án, triệu chứng và các yếu tố khác. 
3. **Lời khuyên thiết thực:** 
    * **Chế độ dinh dưỡng:**  Đưa ra lời khuyên về chế độ ăn uống phù hợp.
    * **Chế độ luyện tập:** Đề xuất các bài tập thể dục phù hợp với tình trạng sức khỏe.
    * **Lối sống:**  Gợi ý thay đổi lối sống để cải thiện sức khỏe (ví dụ:  ngủ đủ giấc, giảm stress).
    * **Theo dõi và thăm khám:** Nhấn mạnh tầm quan trọng của việc theo dõi sức khỏe và  khám bác sĩ định kỳ. 

**Lưu ý:**

* Bài phân tích cần rõ ràng, dễ hiểu và có tính thực tế cao.
* Không được đưa ra lời khuyên chẩn đoán hoặc điều trị y tế cụ thể. 
* Khuyến khích người dùng tìm kiếm sự tư vấn từ chuyên gia y tế.
"""

    return prompt


def getRes(text, type):
    """Generates content based on the provided text and type.

    Args:
        text: The input text for content generation.
        type: The type of content to generate.

    Returns:
        The generated text content, or an error message if generation fails.
    """

    prompt = getPrompt(text, type)
    max_retries = 3  # Adjust as needed
    retry_delay = 5  # Seconds to wait between retries

    for attempt in range(max_retries):
        try:
            response = model.generate_content(prompt)
            return response.text

        except Exception as e:
            print(f"Error during content generation (Attempt {attempt+1}): {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                return "An error occurred during content generation. Please try again later."

    return "Unable to generate content after multiple attempts."
