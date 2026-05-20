FILE_LIST_NAME = 'file_list.csv'
METRICS_NAME = 'metrics.csv'

# Lo hacen ellos desde 0.
def main():
    """Generates the metrics.csv file based on the file list contained in file_list.csv"""
    pass
    
def set_current_directory_to_script_location():
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

if __name__ == '__main__':
    set_current_directory_to_script_location()
    main()