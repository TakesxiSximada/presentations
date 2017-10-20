SCREEN_SHOT_DIR := ~/Desktop


.PHONY: copy
copy:
	@# スクリーンショットをファイル名を変更してコピーする
	for _FILENAME	in `ls $(SCREEN_SHOT_DIR)`; do echo $$_FILENAME; done
