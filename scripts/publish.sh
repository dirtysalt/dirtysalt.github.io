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

function publish-org-html() {
    # 保存上次构建的 commit id 的文件
    LAST_COMMIT_FILE=".last_build_commit"

    # 获取当前最新 commit id
    CURRENT_COMMIT=$(git rev-parse HEAD)

    # 判断是否有历史记录
    if [ -f "$LAST_COMMIT_FILE" ]; then
        LAST_COMMIT=$(cat "$LAST_COMMIT_FILE")
    else
        LAST_COMMIT=""
    fi

    # 比较 commit id
    if [ "$CURRENT_COMMIT" != "$LAST_COMMIT" ]; then
        # 检查是否有修改来自于 src 文件夹
        if [ -z "$LAST_COMMIT" ] || ! git diff --name-only "$LAST_COMMIT" "$CURRENT_COMMIT" | grep -q "^src/"; then
            echo "没有检测到 src 文件夹的修改，不执行构建。"
            return 0
        fi
        echo "检测到新的提交，执行 publish-html.sh ..."
        bash ./scripts/publish-html.sh
        
        if [ $? == 0 ]; then
            CURRENT_COMMIT=$(git rev-parse HEAD)
            echo "$CURRENT_COMMIT" > "$LAST_COMMIT_FILE"
            echo "构建完成，已更新 commit 记录。"
        else
            echo "publish-html.sh 执行失败，请检查错误。"
            return 1
        fi
    else
        echo "没有新的提交，不执行构建。"
    fi
}

echo "********** publish org html **********"
publish-org-html
if [ $? != 0 ]; then
    echo "publish org html failed"
    exit 1
fi

echo "********** build index html **********"
python ./scripts/build-index.py
if [ $? != 0 ]; then
    echo "build index html failed"
    exit 1
fi
