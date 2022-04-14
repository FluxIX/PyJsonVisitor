# PyJsonVisitor
Implements a [JSON](https://en.wikipedia.org/wiki/JSON) parser using the Visitor pattern.

## Table of Contents
1. [Visitor Pattern](#visitor-pattern)
1. [Usage](#usage)
	- [Adapters](#adapters)
		- [Simple Adapters](#simple-adapters)
			- [Provided Simple Adapters](#provided-simple-adapters)
		- [Contextual Adapters](#contextual-adapters)
			- [Provided Contextual Adapters](#provided-contextual-adapters)
	- [Subscriptions](#subscriptions)
	- [Terminal Utility](#terminal-utility)
1. [Acknowledgements](#acknowledgements)

## Visitor Pattern
The [Visitor pattern](https://en.wikipedia.org/wiki/Visitor_pattern) is a structural software pattern which allows the separation of an algorithm from the algorithm's input through the use of contextual event handlers. A `BaseAdapter` class provides the contextual event handlers for different [JSON](https://en.wikipedia.org/wiki/JSON) element types and a child class overrides only the event handlers required by the specific algorithm. Since each adapter is completely independent and a specific algorithm's implementation is separated from the input JSON elements, multiple adapters can process the same JSON element events in parallel without interferrence.

## Usage
Normal usage would consist of writing an [adapter](#adapters) derived from a `BaseAdapter` to handle the published events, although two [subscriptions](#subscriptions) have been provided for external subscriber event publishing and a [terminal utility](#terminal-utility) has been provided to expose the event sequence for adapter development.

### Adapters
There are two categories of adapters provided, [simple adapters](#simple-adapters) and [contextual adapters](#contextual-adapters). The primary difference between the simple adapters and the contextual adapters are amount of scope data stored through the iteration: the simple adapters do not store scope data while the contextual adapters store scope data applicable to the scope.

#### Simple Adapters
The simple adapters provide the following event handlers:

- `before_document_start()`
- `process_document_start()`
- `after_document_start()`
- `before_document_end()`
- `process_document_end()`
- `after_document_end()`
- `before_object_start()`
- `process_object_start()`
- `after_object_start()`
- `before_object_end()`
- `process_object_end()`
- `after_object_end()`
- `before_list_start()`
- `process_list_start()`
- `after_list_start()`
- `before_list_end()`
- `process_list_end()`
- `after_list_end()`
- `before_list_item_start()`
- `process_list_item_start()`
- `after_list_item_start()`
- `before_list_item_end()`
- `process_list_item_end()`
- `after_list_item_end()`
- `before_list_item_value_start()`
- `process_list_item_value_start()`
- `after_list_item_value_start()`
- `before_list_item_value_end()`
- `process_list_item_value_end()`
- `after_list_item_value_end()`
- `before_member_start()`
- `process_member_start()`
- `after_member_start()`
- `before_member_end()`
- `process_member_end()`
- `after_member_end()`
- `before_member_key( name )`
- `process_member_key( name )`
- `after_member_key( name )`
- `before_member_value_start()`
- `process_member_value_start()`
- `after_member_value_start()`
- `before_member_value_end()`
- `process_member_value_end()`
- `after_member_value_end()`
- `before_value( value )`
- `process_value( value )`
- `after_value( value )`

The simple adapters do not store any element scope data.

##### Provided Simple Adapters

- [`BaseAdapter`](https://github.com/FluxIX/PyJsonVisitor/blob/main/src/json_visitor/simple_adapters/base_adapter.py): The parent adapter class from which all other adapters are derived.
- [`CompositeAdapter`](https://github.com/FluxIX/PyJsonVisitor/blob/main/src/json_visitor/simple_adapters/composite_adapter.py): This is an adapter contains a list of other adapters. When an event is handled by the `CompositeAdapter`, the event is published to all adapters the `CompositeAdapter` has in its list. The `CompositeAdapter` inherits from the [`BaseAdapter`](https://github.com/FluxIX/PyJsonVisitor/blob/main/src/json_visitor/simple_adapters/base_adapter.py).
- [`ScopeAdapter`](https://github.com/FluxIX/PyJsonVisitor/blob/main/src/json_visitor/simple_adapters/scope_adapter.py): This adapter builds the element scope for any element as the JSON file is being parsed. The `ScopeAdapter` inherits from the [`BaseAdapter`](https://github.com/FluxIX/PyJsonVisitor/blob/main/src/json_visitor/simple_adapters/base_adapter.py).
- [`ScopeInspectionAdapter`](https://github.com/FluxIX/PyJsonVisitor/blob/main/src/json_visitor/simple_adapters/scope_inspector_adapter.py): This adapter prints the node events from the JSON file to standard output as the JSON file is being parsed; only the `process_*` event handlers are invoked. The `ScopeInspectionAdapter` inherits from the [`ScopeAdapter`](https://github.com/FluxIX/PyJsonVisitor/blob/main/src/json_visitor/simple_adapters/scope_adapter.py).

#### Contextual Adapters
The contextual adapters provide all of the event handlers provided by the simple adapters as well as the following event handlers:

- `before_document( root_scope)`
- `process_document( root_scope )`
- `after_document( root_scope )`
- `before_object( members )`
- `process_object( members )`
- `after_object( members )`
- `before_member( name, value )`
- `process_member( name, value )`
- `after_member( name, value )`
- `before_list( items )`
- `process_list( items )`
- `after_list( items )`
- `before_list_item( index, value )`
- `process_list_item( index, value )`
- `after_list_item( index, value )`

The contextual adapters store the necessary element scope data required to associate an element with the element's subordinate data.

##### Provided Contextual Adapters

- [`BaseAdapter`](https://github.com/FluxIX/PyJsonVisitor/blob/main/src/json_visitor/contextual_adapters/base_adapter.py): The parent adapter class from which all other contextual adapters are derived. The `BaseAdapter` inherits from the [`ScopeAdapter`](https://github.com/FluxIX/PyJsonVisitor/blob/main/src/json_visitor/simple_adapters/scope_adapter.py).
- [`CompositeAdapter`](https://github.com/FluxIX/PyJsonVisitor/blob/main/src/json_visitor/contextual_adapters/composite_adapter.py): This adapter contains a list of other adapters. When an event is handled by the `CompositeAdapter`, the event is published to all adapters the `CompositeAdapter` has in its list. The `CompositeAdapter` inherits from the contextual [`BaseAdapter`](https://github.com/FluxIX/PyJsonVisitor/blob/main/src/json_visitor/contextual_adapters/base_adapter.py).
- [`InspectionAdapter`](https://github.com/FluxIX/PyJsonVisitor/blob/main/src/json_visitor/contextual_adapters/inspector_adapter.py): This adapter prints the node events from the JSON file to standard output as the JSON file is being parsed; only the `process_*` event handlers are invoked. The `InspectionAdapter` inherits from the contextual [`BaseAdapter`](https://github.com/FluxIX/PyJsonVisitor/blob/main/src/json_visitor/contextual_adapters/base_adapter.py) and the [`ScopeInspectionAdapter`](https://github.com/FluxIX/PyJsonVisitor/blob/main/src/json_visitor/simple_adapters/scope_inspector_adapter.py).

#### Default Event Handler Behavior
The event handlers implemented in the `BaseAdapter` classes call a different method based on the event handler's timing; this method as implemented in the simple [`BaseAdapter`](https://github.com/FluxIX/PyJsonVisitor/blob/main/src/json_visitor/simple_adapters/base_adapter.py) class has an empty body but can be overridden in a child class to apply a default behavior to all event handlers with specific timing. The methods are as follows:

- The `before_*` event handlers invoke the `default_before( *args, **kwargs )` method.
- The `process_*` event handlers invoke the `default_process( *args, **kwargs )` method.
- The `after_*` event handlers invoke the `default_after( *args, **kwargs )` method.

#### Subscriptions
Two subscriptions are provided for event consumption by adapter-external subscribers. Callbacks are registered with the subscription using the `register( subscription_key, callback )` method; valid subscription keys are retrieved using the `subscription_keys` property.

- [`SimpleSubscription`](https://github.com/FluxIX/PyJsonVisitor/blob/main/src/json_visitor/subscription/simple_subscription.py): This subscription publishes the events in the simple [`BaseAdapter`](https://github.com/FluxIX/PyJsonVisitor/blob/main/src/json_visitor/simple_adapters/base_adapter.py).
- [`ContextualSubscription`](https://github.com/FluxIX/PyJsonVisitor/blob/main/src/json_visitor/subscription/contextual_subscription.py): This subscription publishes the events in the contextual [`BaseAdapter`](https://github.com/FluxIX/PyJsonVisitor/blob/main/src/json_visitor/contextual_adapters/base_adapter.py).

### Terminal Utility
If the `json_visitor` package is invoked on the terminal (using `python3 -m json_visitor`), the [`InspectionAdapter`](https://github.com/FluxIX/PyJsonVisitor/blob/main/src/json_visitor/contextual_adapters/inspector_adapter.py) prints out the JSON element nodes in a given input source. The utility's help describes the options and inputs supported:

    usage: json_visitor [-h] [-i | -I] [-f <file path>] [-s <string literal>]

    Processes the input JSON strings or files and outputs the visitation events.

    optional arguments:
      -h, --help            show this help message and exit
      -i, --output-processing-info
                            Enables the output of the processing information. This
                            is the default.
      -I, --suppress-processing-info
                            Suppresses the output of the processing information.
      -f <file path>, --file <file path>
                            JSON file path to process; relative paths are relative
                            to the current working directory.
      -s <string literal>, --string <string literal>
                            JSON string literal to process.

The command (on Linux) `python3 -m json_visitor -s "{ \"v\": [ 1, 2,3, 4, 5, 6, { \"key0\": \"value\", \"key1\": {} }] }"` results in the following output:

    document_start
    object_start
    member_start
    member_key: (0: v)
    member_value_start
    list_start
    list_item_start
    list_item_value_start
    value: (0: 1)
    list_item_value_end
    list_item_end
    process_list_item: (0: 0), (1: 1)
    list_item_start
    list_item_value_start
    value: (0: 2)
    list_item_value_end
    list_item_end
    process_list_item: (0: 1), (1: 2)
    list_item_start
    list_item_value_start
    value: (0: 3)
    list_item_value_end
    list_item_end
    process_list_item: (0: 2), (1: 3)
    list_item_start
    list_item_value_start
    value: (0: 4)
    list_item_value_end
    list_item_end
    process_list_item: (0: 3), (1: 4)
    list_item_start
    list_item_value_start
    value: (0: 5)
    list_item_value_end
    list_item_end
    process_list_item: (0: 4), (1: 5)
    list_item_start
    list_item_value_start
    value: (0: 6)
    list_item_value_end
    list_item_end
    process_list_item: (0: 5), (1: 6)
    list_item_start
    list_item_value_start
    object_start
    member_start
    member_key: (0: key0)
    member_value_start
    value: (0: value)
    member_value_end
    member_end
    process_member: (0: key0), (1: value)
    member_start
    member_key: (0: key1)
    member_value_start
    object_start
    object_end
    process_object: (0: {})
    member_value_end
    member_end
    process_member: (0: key1), (1: {})
    object_end
    process_object: (0: {'key0': 'value', 'key1': {}})
    list_item_value_end
    list_item_end
    process_list_item: (0: 6), (1: {'key0': 'value', 'key1': {}})
    list_end
    process_list: (0: (1, 2, 3, 4, 5, 6, {'key0': 'value', 'key1': {}}))
    member_value_end
    member_end
    process_member: (0: v), (1: (1, 2, 3, 4, 5, 6, {'key0': 'value', 'key1': {}}))
    object_end
    process_object: (0: {'v': (1, 2, 3, 4, 5, 6, {'key0': 'value', 'key1': {}})})
    document_end
    process_document: (0: {'v': (1, 2, 3, 4, 5, 6, {'key0': 'value', 'key1': {}})})
    Number of scope events processed: 103

## Acknowledgements
The hard work of turning JSON into an event stream is done by the [`ijson`](https://pypi.org/project/ijson/) package, without which the Visitor interface would have been much more challenging to develop.
