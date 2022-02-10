MENU_PROMPT = """
    1.- To create a blog
    2.- To list blogs 
    3.- To read one 
    4.- To create a post
    0.- Exit 
    """
blogs = dict() 

def menu(): 
    # Show the user the available blogs
    # Let the user make a choice 
    # Do something with that choice 
    # Eventually exit 
    
    print_blogs()
    selection = int(input(MENU_PROMPT))
    

def print_blogs():
    for key, blog in blogs.items(): 
        print(f"{blog}")

def start(): 
    menu() 

if __name__ == "__main__":
    start()