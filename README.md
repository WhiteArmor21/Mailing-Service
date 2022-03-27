# Mailing-Service
Test project
all the requirements set in the requirements.txt
The project is divided into two applications:
                                -clients (provides clients services),
                                -mailing (provides mailing and messages services).
This project provides simple mailing service:
includes models:
         -Client model stores:
                       -client id,
                       -phone number,
                       -mobile operator (mobile operator code),
                       -tag (for client filter),
                       - client  timezone.
         -Mailing model stores:
                       -mailing id,
                       -start_time,
                       -message,
                       -mobile_operator (optional field for mailing targeting),
                       -tag (optional field for mailing targeting),
                       -completion_time,
                       -counter (field that counts all messages sended by this mailing).
         -Message model stores:
                       -create_time,
                       -status,
                       -mailing (fk to mailing),
                       -client (fk to client).
API's: 
      -127.0.0.1:8000/admin/ - classic django admin interface,
      -127.0.0.1:8000/clients/ - Clients list,
      -127.0.0.1:8000/clients/add/ - register new client,
      -127.0.0.1:8000/clients/<int:id>/ - detail info about client with {client id} and tools for update or delete this client,
      -127.0.0.1:8000/mailings/ - Mailings list,
      -127.0.0.1:8000/mailings/add/ - register new mailing,
      -127.0.0.1:8000/mailings/<int:id>/ - detail info about mailing with {mailing id} and tools for update or delete this mailing,
      -127.0.0.1:8000/mailings/<int:id>/messages/ - detail message info filtered by mailing
      -127.0.0.1:8000/mailings/<int:id>/send/ - create new message, send it to testing server, and save this message to db.
      
