prompt = \
'''
<task>
You have to read HTML data in order to answer some questions.
The HTML data and the questions are related to an italian rent property.
Stick to the content provided, if you can't answer any questions, leave it blank.
Use <output> to generate your answer.
</task>

<instruction>
1. Inside <data> you will find the html data.
2. Read <data>
3. Answer the following questions in the specified tag:
    3.1 <question> Are there more than 3 bedrooms? How many?</question> <tag>bedrooms</tag>
    3.2 <question> Which type of rent contract is? (4+4, cedolare, ...)</question> <tag>rent-contract</tag>
    3.3 <question> Where the property is located? specify street infos.</question> <tag>location</tag>
    3.4 <question> What is written under 'Arredato'?</question> <tag>arredato</tag>
    3.5 <question> How many bathrooms are there? tip: look under 'Bagni'</question> <tag>bathrooms</tag>
    3.6 <question> Is it mentioned in the text if the house is exclusively offered to students?</question> <tag>student-only</tag>

Here is an example of how your output must be:
<example>

<output>
<bedrooms>There are 4 bedrooms.</bedrooms>
<rent-contract>The type of rent contract is 4+4 with cedolare secca.</rent-contract>
<location>The property is located in...</location>
<arredato>Completly furnished.</arredato>
<bathrooms>There are 2 bathrooms.</bathrooms>
</output>

</example>

</instruction>

<data>
{data}
</data>
'''

prompt_analysis = \
'''
<task>
You have to read XML data to analyse it based oh the specified requirements.
The XML data are related to an italian rent property.
Use <output> to generate your answer.
</task>

<instruction>
1. Inside <data> you will find the XML data.
2. Read <data>
3. Add an item to your response based on <info>, check if the item meet the following requirements:
    1. There are at least 3 Bedrooms.
    2. Contract type IS everyting besides 4+4, so if it's just 'affitto' it is actually fine
    3. The house must me available for workers
    
Here is an example of how your output must be:
<example>

<output>
113714857
113714858
</output>

</example>
</instruction>

<data>
{data}
</data>
'''
