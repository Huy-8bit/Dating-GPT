// ở đây sẽ gọi hàm random 3 câu để thay thế dữ liệu choise


const suggest = async (req,res)=>{
    const choise = ["nam1","nam2","nam3"]
    res.json(choise) 
}

module.exports = suggest