import os
import yaml


yaml_file_path = os.path.dirname(__file__) + "/data.yml"
with open(yaml_file_path, "r", encoding="utf-8") as f:
    datasa = yaml.safe_load(f)
    print(datasa)
    datas = datasa["datas"]
    ids = datasa["ids"]
    print(datas)
    print(ids)




if __name__ == '__main__':
    python.main(['-vs'])