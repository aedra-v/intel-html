def parse_throne(event, context):
    resource_string = context.resource
    trigger_docid = resource_string.split('/')[-1]
    print(f"Function triggered by change to: {resource_string}.")
    print(str(event))

    importhtml = event['importhtml']

    inteltable = pd.read_html(importhtml)
    print(inteltable)

    soup = BeautifulSoup(event[importhtml], 'html.parser')
    print(soup)

    return f'Success'
