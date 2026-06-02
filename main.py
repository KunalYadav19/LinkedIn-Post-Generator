from config import get_model
from user_input     import collect_inputs  
from prompt_builder import generate_post   

def save(post, topic): 
    import re
    safe_name = re.sub(r'[^a-zA-Z0-9_]', '_', topic.strip())
    filename = f"LINKDIN_POST_{safe_name}.txt"
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(post)

    return filename

def run():
    """
    Main Pipeline
    sara execution yaha se control hoga
    """
    
    try:
        model = get_model()
    
    except Exception as e:
        print(e)

    inputs = collect_inputs()

    try:
      post = generate_post(model, inputs)
    except Exception as e:
        print(e)

    print(post)

    filename = save(post,inputs['topic'])
    print('File saved successfully: ',filename )

if __name__ == "__main__":
    run()
