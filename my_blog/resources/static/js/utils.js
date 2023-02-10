// 历史上的今天滚动时间
const HISTORY_ROLL_TIME = 3 * 1000;

// 默认主题
const DEFAULT_STYLE = 'jianyue';

// 畅言云评配置
const JY_APPID = 'cywaAMztL';
const JY_CONF = 'e3824b9a4697f932a57c2e8ee8c99600'

// 设置历史上的今天
function set_history_day () {
    let _url = "https://v2.alapi.cn/api/eventHistory?token=LYZn3pVn2Xr7HBUf&monthday=";
    let date = new Date();
    // 获取今天的日期0101
    let _month = date.getMonth() + 1
    let _day = date.getDate()
    let day = String(((_month < 10) ? "0" + _month : _month)) + String(((_day < 10) ? "0" + _day : _day))

    // 请求json
    $.ajax({
        url: _url + day,
        type: "GET",
        success:(data)=>{
            $history_tag = $('#history');
            $history_tag.html(data["data"][0]["year"] + "年" + data["data"][0]["title"]);

            setInterval(() => {
                // $history_tag.html(data["data"][i]["year"] + data["data"][i]["title"]);
                $history_tag.html(data["data"][i]["year"] + "年" + data["data"][i]["title"]);
                i = (i < data["data"].length - 1) ? i + 1 : 0;
            }, HISTORY_ROLL_TIME , i=1 )
        }
    })
};

