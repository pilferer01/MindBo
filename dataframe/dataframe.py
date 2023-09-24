# В датафреймах (pyspark.sql.DataFrame) заданы продукты, категории и связь между ними.
# Одному продукту может соответствовать много категорий, в одной категории может быть много продуктов.
# Напишите метод с помощью PySpark, который вернет все продукты с их категориями
# (датафрейм с набором всех пар «Имя продукта – Имя категории»). В результирующем датафрейме должны также присутствовать
# продукты, у которых нет категорий.

from pyspark.sql import SparkSession

# Создание spark session
spark = (
    SparkSession.builder
    .master("local")
    .appName("Word Count")
    .getOrCreate()
)
# Я бы мог сделать загрузку dataframe с csv или другого файла,но мне кажется так наглядней.
# DATAFRAME продуктов
productDF = spark.createDataFrame([
    {"id": 1, "name": "Куриная ножка"},
    {"id": 2, "name": "Картошка"},
    {"id": 3, "name": "Филе"},
    {"id": 4, "name": "Банан"},
    {"id": 5, "name": "Хлеб"}
])
# DATAFRAME категорий
categoryDF = spark.createDataFrame([
    {"id": 1, "name": "Рыба и рыбные продукты"},
    {"id": 2, "name": "Мясо"},
    {"id": 3, "name": "Плодоовощные товары"},
    {"id": 4, "name": "Молочные продукты"},
    {"id": 5, "name": "Фрукты"}
])
# DATAFRAME связей
relationDF = spark.createDataFrame([
    {"product_id": 1, "category_id": 2},
    {"product_id": 2, "category_id": 3},
    {"product_id": 3, "category_id": 1},
    {"product_id": 4, "category_id": 3},
    {"product_id": 4, "category_id": 5},
    {"product_id": 5, "category_id": 6}
])

# создание результирующего dataframe через join
resultDF = (relationDF.join(productDF, relationDF.product_id == productDF.id, 'left')
            .join(categoryDF, relationDF.category_id == categoryDF.id, 'left')
            .select(productDF["name"].alias("product_name"), categoryDF["name"].alias("category_name")))

print("Через join:")
resultDF.show(truncate=False)

productDF.createOrReplaceTempView("Product")
categoryDF.createOrReplaceTempView("Category")
relationDF.createOrReplaceTempView("Relation")

# Сделал второй варианта, чтобы показать что и так можно
# создание результирующего dataframe через sql
resultDF = (spark.sql("SELECT P.name as product_name, C.name as category_name FROM Product P"
                      " LEFT JOIN Relation R ON P.id == R.product_id"
                      " LEFT JOIN Category C ON C.id == R.category_id"))
print("Через sql запрос:")
resultDF.show(truncate=False)

