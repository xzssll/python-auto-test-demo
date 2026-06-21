import yaml
import traceback
from jsonpath import jsonpath as jp
from Src.utils.handle_data import replace_dynamic_params


# def callback(Loader,node):
   
#     return get_token



# class Yamloader:
#     def __init__(self,tags = [{"!get_token":callback},]):
#         for tag in tags:
#             for k,v in tag.items():
#                 yaml.add_constructor(k,v,yaml.SafeLoader)

class Yamloader:
    def yamloader(self,file_path):
        try:
            with open(file=file_path,mode="r",encoding="utf-8") as f:
                result = yaml.load(stream=f.read(),Loader=yaml.SafeLoader)
            return result
        except Exception as e:
            traceback.print_exc()
            return None

# if __name__ == "__main__":
#     print(yamloader(file_path))