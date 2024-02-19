import os

# Copy and paste your OpenAI API Key
openai_api_key = os.getenv("OPENAI_API_KEY")
# Put your name
key_owner = "John Doe"

maze_assets_loc = "../../environment/frontend_server/static_dirs/assets"
env_matrix = f"{maze_assets_loc}/the_ville/matrix"
env_visuals = f"{maze_assets_loc}/the_ville/visuals"

fs_storage = "../../environment/frontend_server/storage"
fs_temp_storage = "../../environment/frontend_server/temp_storage"

collision_block_id = "32125"

# Verbose 
debug = True

# models
class gpt_structure_models():
    ChatGPT_single_request = "gpt-3.5-turbo"
    ChatGPT_request = "gpt-3.5-turbo"
    GPT4_request = "gpt-4"

class run_gpt_prompt_models():
    #v1
    action_location_sector_v1 ="gpt-3.5-turbo-instruct"
    action_location_object_vMar11 ="gpt-3.5-turbo-instruct"
    action_object_v2 ="gpt-3.5-turbo-instruct"
    #v2
    create_conversation_v2 ="gpt-3.5-turbo-instruct"
    convo_to_thoughts_v1= "gpt-3.5-turbo-instruct"
    daily_planning_v6 ="gpt-3.5-turbo-instruct"
    decide_to_talk_v2 ="gpt-3.5-turbo-instruct"
    decide_to_react_v1 ="gpt-3.5-turbo-instruct"
    generate_hourly_schedule_v2 ="gpt-3.5-turbo-instruct"
    generate_event_triple_v1 ="gpt-3.5-turbo-instruct"
    get_keywords_v1 ="gpt-3.5-turbo-instruct"
    generate_focal_pt_v1 ="gpt-3.5-turbo-instruct"
    insight_and_evidence_v1 ="gpt-3.5-turbo-instruct"
    keyword_to_thoughts_v1 ="gpt-3.5-turbo-instruct"
    new_decomp_schedule_v1 = "gpt-3.5-turbo-instruct"
    planning_thought_on_convo_v1 ="gpt-3.5-turbo-instruct"
    task_decomp_v3 = "gpt-3.5-turbo-instruct"
    wake_up_hour_v1 = "gpt-3.5-turbo-instruct"
    whisper_inner_thought_v1 = "gpt-3.5-turbo-instruct"
    #v3 chatgpt
    agent_chat_v1 = "gpt-3.5-turbo-instruct"
    generate_pronunciatio_v1 ="gpt-3.5-turbo-instruct"
    generate_obj_event_v1 ="gpt-3.5-turbo-instruct"
    generate_focal_pt_v1 = "gpt-3.5-turbo-instruct"
    generate_next_convo_line_v1 ="gpt-3.5-turbo-instruct"
    iterative_convo_v1 = "gpt-3.5-turbo-instruct"
    memo_on_convo_v1 ="gpt-3.5-turbo-instruct"
    poignancy_event_v1 = "gpt-3.5-turbo-instruct"
    poignancy_thought_v1 ="gpt-3.5-turbo-instruct"
    poignancy_chat_v1 ="gpt-3.5-turbo-instruct"
    summarize_conversation_v1 ="gpt-3.5-turbo-instruct"
    summarize_chat_ideas_v1 = "gpt-3.5-turbo-instruct"
    summarize_chat_relationship_v2 ="gpt-3.5-turbo-instruct"
    summarize_ideas_v1 ="gpt-3.5-turbo-instruct"
    #safety
    anthromorphosization_v1 = "gpt-3.5-turbo-instruct"

class defunct_run_gpt_models():
    #v1
    action_object_v2 = "gpt-3.5-turbo-instruct"
    action_location_object_v1 = "gpt-3.5-turbo-instruct"
    action_location_sector_v2 = "gpt-3.5-turbo-instruct"
    
    #v2
    agent_chat_v1 = 'gpt-3.5-turbo-instruct'
    convo_to_thoughts_v1 = 'gpt-3.5-turbo-instruct'
    create_conversation_v2 = 'gpt-3.5-turbo-instruct'
    daily_planning_v6 = 'gpt-3.5-turbo-instruct'
    decide_to_react_v1 = 'gpt-3.5-turbo-instruct'
    decide_to_talk_v2 = 'gpt-3.5-turbo-instruct'
    generate_event_triple_v1 = 'gpt-3.5-turbo-instruct'
    generate_hourly_schedule_v2 = 'gpt-3.5-turbo-instruct'
    generate_obj_event_v1 = 'gpt-3.5-turbo-instruct'
    generate_pronunciatio_v1 = 'gpt-3.5-turbo-instruct'
    get_keywords_v1 = 'gpt-3.5-turbo-instruct'
    generate_focal_pt_v1 = 'gpt-3.5-turbo-instruct'
    generate_next_convo_line_v1 = ''
    insight_and_evidence_v1 = 'gpt-3.5-turbo-instruct'
    keyword_to_thoughts_v1 = 'gpt-3.5-turbo-instruct'
    new_decomp_schedule_v1 = 'gpt-3.5-turbo-instruct'
    poignancy_event_v1 = 'gpt-3.5-turbo-instruct'
    poignancy_thought_v1 = 'gpt-3.5-turbo-instruct'
    poignancy_chat_v1 = 'gpt-3.5-turbo-instruct'
    planning_thought_on_convo_v1 = 'gpt-3.5-turbo-instruct'
    summarize_conversation_v1 = 'gpt-3.5-turbo-instruct'
    summarize_chat_ideas_v1 = 'gpt-3.5-turbo-instruct'
    summarize_chat_relationship_v1 = 'gpt-3.5-turbo-instruct'
    summarize_ideas_v1 = 'gpt-3.5-turbo-instruct'
    task_decomp_v3 = 'gpt-3.5-turbo-instruct'
    wake_up_hour_v1 = 'gpt-3.5-turbo-instruct'
    whisper_inner_thought_v1 = 'gpt-3.5-turbo-instruct'
    memo_on_convo_v1 = 'gpt-3.5-turbo-instruct'
