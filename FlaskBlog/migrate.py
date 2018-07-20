#coding:utf-8
#说明：执行数据库迁移的脚本文件

from app import appweb,db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

migrate = Migrate(appweb,db)
manager = Manager(appweb)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()