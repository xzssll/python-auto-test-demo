# Src/utils/handle_data.py
import json

def replace_dynamic_params(data, replace_data):
    """
    data: 从 YAML 读出来的原始字典
    replace_dict: 必须是一个字典，例如 {"token": "实际的token字符串"}
    """
    # 1. 拍平成字符串
    data_str = json.dumps(data, ensure_ascii=False)
    
    # 2. 循环字典进行替换
    for key, value in replace_data.items():
        # 寻找 ${token} 这种格式并替换
        placeholder = f"${{{key}}}" 
        data_str = data_str.replace(placeholder, str(value))
    
    # 3. 还原成字典
    return json.loads(data_str)