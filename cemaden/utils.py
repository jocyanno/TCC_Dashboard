from db_utils import create_connection, insert_data, connection_close

def process_and_store_data(response):
  connection = create_connection()
  data = response.json()
  for record in data:  
    data_tuple = (
      record["acc120hr"], record["acc12hr"], record["acc1hr"], record["acc24hr"],
      record["acc3hr"], record["acc48hr"], record["acc6hr"], record["acc72hr"],
      record["acc96hr"], record["codestacao"], record["codibge"],
      record["datahora"], record["id_estacao"]
    )
    insert_data(connection, data_tuple)
  connection_close(connection)