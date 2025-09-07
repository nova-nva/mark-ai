from ..schemas.state import FlowState

def route(state: FlowState) -> str:
    if state.route == "start":
        return "start"
    
    if state.route == "break":
        return "stop"
    
    # after HIA
    if state.route == "start":
        return state.next_after_hia()
    
    if state.route == "copywriter":
        return "stop"
    
    return "stop"