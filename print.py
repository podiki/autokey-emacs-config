# set the actions
hotkey = '<super>+p'
newkey = '<ctrl>+p'

# save the hotkey for pasthrough 
store.set_global_value('hotkey', hotkey)

# set the new key
engine.set_return_value(newkey)

# proces the key
engine.run_script('process_key')

# we should turn off shift
ignored = store.get_global_value('ignored')
if not ignored:
    store.set_global_value('shift_on', False)

