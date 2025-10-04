#!/bin/bash
# publish org files.

# clean trash files
rm -rf images/\.#*
rm -rf src/\.#*
rm -rf html/\.#*

echo "********** check references **********"
python3 ./scripts/check-image-ref.py `pwd`
if [ $? != 0 ]; then
    echo "resolve image ref issues!"
    exit 1
fi

echo "********** enforce org format **********"
python $HOME/.private/project/pyscript/utils/enforce-org-format.py `pwd`
if [ $? != 0 ]; then
    echo "enforce org format failed"
    exit 1
fi

echo "********** rename org images **********"
python $HOME/.private/project/pyscript/utils/rename-org-images.py `pwd`/images
if [ $? != 0 ]; then
    echo "rename org images failed"
    exit 1
fi

echo "********** compress images **********"
python $HOME/.private/project/pyscript/utils/compress-images.py `pwd`/images
if [ $? != 0 ]; then
    echo "compress images failed"
    exit 1
fi

function org-export-html() {
    # 保存上次构建的 commit id 的文件
    LAST_COMMIT_FILE=".org_export_last_commit"

    # 获取当前最新 commit id
    CURRENT_COMMIT=$(git rev-parse HEAD)

    # 判断是否有历史记录
    if [ -f "$LAST_COMMIT_FILE" ]; then
        LAST_COMMIT=$(cat "$LAST_COMMIT_FILE")
    else
        LAST_COMMIT=$(git rev-parse HEAD)
    fi

    # 比较 commit id
    if [ "$CURRENT_COMMIT" != "$LAST_COMMIT" ]; then        
        # 检查是否有修改来自于 src 文件夹
        echo "LAST_COMMIT: $LAST_COMMIT, CURRENT_COMMIT: $CURRENT_COMMIT"
        git diff --name-only "$LAST_COMMIT" "$CURRENT_COMMIT" | grep -q "^src/*.org"
        if ! git diff --name-only "$LAST_COMMIT" "$CURRENT_COMMIT" | grep -q "^src/*.org"; then
            echo "没有检测到 src 文件夹的修改，不执行构建。"
            return 0
        fi
        echo "检测到新的提交，执行 org-export-html.sh ..."
        bash ./scripts/org-export-html.sh
        
        if [ $? == 0 ]; then
            CURRENT_COMMIT=$(git rev-parse HEAD)
            echo "$CURRENT_COMMIT" > "$LAST_COMMIT_FILE"
            echo "构建完成，已更新 commit 记录。"
        else
            echo "org-export-html.sh 执行失败，请检查错误。"
            return 1
        fi
    else
        echo "没有新的提交，不执行构建。"
    fi
}

echo "********** org export html **********"
org-export-html
if [ $? != 0 ]; then
    echo "org export html failed. ignore this error."
    exit 1
fi