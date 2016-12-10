# Grouped Bar Plot
x <-c("Frontier", "Morden", "Ropsten")
#gzip
y1<-c(10.1, 9,12)
y2<-c(18, 13.7,17.7)
#bzip2
#y1 <- c(9.2, 5.0, 7.8)
#y2<-c(15.8, 10.1, 13.9)
#xz
#y1<-c(9.3, 9.6,16.2)
#y2<-c(11.3, 12.7,19.4)
data<-data.frame(row.names=x,y1,y2)
bp<-barplot(t(as.matrix(data)), ylim=c(0,26),
         ylab="Percentage gains", col=c("red","dark green"),
        legend = c("with Huffman Coding", "without Huffman Coding"), beside=TRUE)
text(bp, round(t(as.matrix(data)),1), round(t(as.matrix(data)), 1),cex=1,pos=3) 
