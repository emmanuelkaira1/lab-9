<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Список посещенных городов</title>
    <style>
        body {
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
        }
        form {
            margin-bottom: 20px;
        }
        input[type="text"],
        input[type="date"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 4px;
            border: 1px solid #ccc;
        }
        input[type="submit"] {
            background-color: #007bff;
            color: #fff;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #0056b3;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #007bff;
            color: #fff;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Список посещенных городов</h1>
        <form action="/add" method="post">
            <input type="text" name="city" placeholder="Введите название города" required>
            <!-- Set the min attribute to today's date -->
            <input type="date" name="visit_date" max="{{ date.today() }}" required>
            <input type="submit" value="Добавить город">
        </form> <!-- Closing the first form tag here -->
        <form action="/clear" method="post">
            <input type="submit" value="Clear">
        </form>
        <table>
            <tr>
                <th>Город</th>
                <th>Дата посещения</th>
            </tr>
            {% for city in cities %}
            <tr>
                <td>{{ city.name }}</td>
                <td>{{ city.visit_date }}</td>
            </tr>
            {% endfor %}
        </table>
    </div>
</body>
</html>