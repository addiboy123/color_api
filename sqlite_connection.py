import sqlite3 as sq
db=sq.connect(database='connection.db',check_same_thread=False)
cur=db.cursor()


def get():
    color_list=[]
    q2="select * from colors"
    cur.execute(q2)
    for i in cur:
       color_list.append({'id':i[0],'color':i[1],'value':i[2]})

    return color_list


def get_one(id):
    q2=f"select * from colors where id={id}"
    cur.execute(q2)
    for i in cur:
        return {'id':i[0],'color':i[1],'value':i[2]}

def post(color,value):
    q1="Insert into colors values(NULL,?,?)"
    cur.execute(q1,(color,value))
    db.commit()

def put(id,color,value):
    q1=f"update colors set color={color},value={value} where id={id}"
    cur.execute(q1)
    db.commit()

def delete(id):
    q1=f"delete from colors where id={id}"
    cur.execute(q1)
    db.commit()


if __name__=='__main__':

    color_data=[
        [0,"red","#f00"],
        [1,"green","#0f0"],
        [2,"blue","#00f"],
        [3,"cyan","#0ff"],
        [4,"magenta", "#f0f"],
        [5,"yellow","#ff0"],
        [6,"black","#000"]
    ]
        
    Q=""" Create table colors(
        id integer primary key autoincrement,
        color varchar(20),
        value varchar(10)
    )"""
    
    q1="Insert into colors values(?,?,?)"
    cur.execute(Q)
    cur.executemany(q1,color_data)

    # post('orange','#FFA500')
    db.commit()
    # print(get())
        
   

    db.close()