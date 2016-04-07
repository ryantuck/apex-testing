import dataset

def handle(event, context):

    # define login creds
    user = 'ryan'
    passwd = 'ryanryan'
    host = 'playground.ct8hgxfp9kz9.us-west-2.rds.amazonaws.com'
    port = '5432'
    db = 'petstore'
    dialect = 'postgres'


    # assemble location string
    location = '{dialect}://{user}:{passwd}@{host}:{port}/{db}'.format(
            dialect=dialect,
            user=user,
            passwd=passwd,
            host=host,
            port=port,
            db=db
            )

    db = dataset.connect(location)
    table = db['pets'].all()

    return [dict(x) for x in table]

