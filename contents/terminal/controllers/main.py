from models.database import Database
from views.headers import welcome
from views.menus import operation_crud
from models.articles import Article

def run_app(DATABASE):
    welcome()
    db = Database(DATABASE)
    #operation_crud()
    print(db.create_table(Article))
    #conn = get_connection(DATABASE)
    #create_table(conn, "articulos")
    #conn.close()
