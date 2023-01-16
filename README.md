**SPD** is a script written in python that prints the **service name** and **description** for a given **port number**

**Requirement:**
> ```sh
> pip install prettytable
> ```

**Usage**:
> ```sh
> python spd.py <port_number>
> ```
**Example**:
> ```sh
> python spd.py 389
> ```
>
> |**Port Number**|**Service Name**|**Description**|
> |:-:|:-:|:-:|
> |**389**|**ldap**|**Lightweight Directory Access Protocol**|

The json file `spd.json`(just an abbrevation for Services Names, Port Numbers, Description) is a filtered version of [Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)
