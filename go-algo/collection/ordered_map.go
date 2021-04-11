package collection

type OrderedMapItem struct {
	Key, Value interface{}
	Prev, Next *OrderedMapItem
}

type OrderedMap struct {
	dict       map[interface{}]*OrderedMapItem
	head, tail *OrderedMapItem
}

func NewOrderedMap() *OrderedMap {
	dict := map[interface{}]*OrderedMapItem{}
	return &OrderedMap{dict: dict}
}

func (om *OrderedMap) Set(key, val interface{}) {
	if om.dict[key] != nil {
		om.dict[key].Value = val
		return
	}
	omi := om.push(key, val)
	om.dict[key] = omi
}

func (om *OrderedMap) Get(key interface{}) (val interface{}, found bool) {
	if om.dict[key] == nil {
		return nil, false
	}
	return om.dict[key].Value, true
}

func (om *OrderedMap) Delete(key interface{}) {
	item := om.dict[key]
	if item != nil {
		if item.Prev != nil {
			item.Prev.Next = item.Next
		}
		if item.Next != nil {
			item.Next.Prev = item.Prev
		}
		delete(om.dict, key)
	}
}

func (om *OrderedMap) Front() *OrderedMapItem {
	return om.head
}

func (om *OrderedMap) Back() *OrderedMapItem {
	return om.tail
}

func (om *OrderedMap) push(key, val interface{}) *OrderedMapItem {
	omi := &OrderedMapItem{Key:key, Value:val}
	if om.head == nil {
		om.head = omi
		om.tail = omi
	} else {
		om.tail.Next = omi
		omi.Prev = om.tail
		om.tail = omi
	}
	return omi
}
