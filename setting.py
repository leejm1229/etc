'''
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Project Label",
            "type": "shell",
            "command": "python",
            "args": [
                "${file}"
            ],
            "presentation": {
                "reveal": "always",
                "panel": "new"
            },
            "options": {
                "env": {
                    "PYTHONIOENCODING": "UTF-8"
                }
            },
            "group": {
                "kind": "build",
                "isDefault": true
            }
        }
    ]
}
'''

'''
json 경로 : View -> command palette -> tasks :configure tasks -> create tasks.json.file -> other
'''

'''
깃 토큰 : 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
'''