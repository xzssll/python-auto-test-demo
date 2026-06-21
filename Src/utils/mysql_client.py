import pymysql

DBCONFIG1 = {
    "host":"www.liuyanzu.tech",
    "port":33060,
    "user":"students",
    "password":"1qaz!QAZ123",
    "db":"taskDB"
    
    }
DBCONFIG2 = {
    "host":"www.liuyanzu.tech",
    "port":33060,
    "user":"students",
    "password":"1qaz!QAZ123",
    "db":"ljtestdb"
    }
# 连接数据库
# db = pymysql.connect(host=DBCONFIG["host"],
#                 port=DBCONFIG["port"],
#                 user=DBCONFIG["user"],
#                 password=DBCONFIG["password"],
#                 db=DBCONFIG["db"])
# python解包的方式
class MysqlClient:
    @classmethod
    def query(cls,sql,args=None):
        """
        查询数据返回query_result
        """
        db = pymysql.connect(**DBCONFIG1)
        cursor = db.cursor()
        query_result = ()

        try:
            cursor.execute(sql,args)
            query_result = cursor.fetchall()
            return query_result
        except Exception as e:
            print(f"Error: {e}")
            return () # 失败返回空元组
        finally:
            cursor.close()
            db.close()
    @classmethod
    def commit(cls,sql,args=None):
        """
        修改数据，成功返回True，否则返回false
        """
        db = pymysql.connect(**DBCONFIG1)
        cursor = db.cursor()
        try:
            res = cursor.execute(sql,args)
            db.commit()
            return True if res else False

        except:
            db.rollback()
            cursor.close()
            db.close()
            return False
        finally:
            cursor.close()
            db.close()


# if __name__ == "__main__":
#     print("---------")  
#     res = MysqlClient.query(sql = "select phone from tb_user where phone = '19912341110'and status = 1")
#     print(res[0][0])
