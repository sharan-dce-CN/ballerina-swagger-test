import sys
import os



ballerina_file_path = sys.argv[1]
folder_path = os.path.dirname(ballerina_file_path)
current_path = os.getcwd()
os.chdir(folder_path)
os.system('ballerina run ' + ballerina_file_path.split('/')[-1] + ' &')
os.chdir(current_path)
os.system('ballerina openapi export ' + ballerina_file_path + ' &')
yaml_file_path = (ballerina_file_path[: -4] + ".openapi.yaml").split('/')[-1]
print(yaml_file_path)
os.system('cat ' + yaml_file_path + ' | python3 swagger-to-html.py > doc.html')
os.system('python3 html_Serve.py')
