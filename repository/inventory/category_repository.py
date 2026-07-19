# internal's import's
from database.connection import DatabaseConnection
from domain.inventory.category import Category


class CategoryRepository:
  def save(self, category: Category) -> None:

    connection = DatabaseConnection.get_connection()

    try:
      cursor = connection.cursor()

      cursor.execute(
        '''
        INSERT INTO category (
          category_name
        )
        VALUES (%s)
        ''',
        (
          category.category_name,
        )
      )
      
      connection.commit()
    
    finally:
      connection.close()