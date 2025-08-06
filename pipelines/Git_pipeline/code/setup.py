from setuptools import setup, find_packages
setup(
    name = 'Git_pipeline',
    version = '1.0',
    packages = find_packages(include = ('git_pipeline*', )) + ['prophecy_config_instances.git_pipeline'],
    package_dir = {'prophecy_config_instances.git_pipeline' : 'configs/resources/git_pipeline'},
    package_data = {'prophecy_config_instances.git_pipeline' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.0.11'],
    entry_points = {
'console_scripts' : [
'main = git_pipeline.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
