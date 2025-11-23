from datetime import datetime

def log(msg: str):
    hour = datetime.now().strftime("%H:%M:%S")
    hour_text = f"[{hour}]:"
    
    if ":" in msg: 
        new_text = msg.replace(":", hour_text)
    else: 
        new_text = msg
        
    print(new_text)