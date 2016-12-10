# Grouped Bar Plot
x <-c("Frontier (size=3.4GB)", "Morden (size=2.2GB)", "Ropsten (size=0.1GB)")
y1 <- c(40.7, 50.5, 55.0)
y2<-c(39.6, 47.4, 51.5)
data<-data.frame(row.names=x,y1,y2)
bp<-barplot(t(as.matrix(data)), ylim=c(0, 75), 
            names.arg=x, ylab="Percentage gains", col=c("red","dark green"),
            legend = c("with Huffman Coding", "without Huffman Coding"), beside=TRUE)
text(bp, round(t(as.matrix(data)),1), round(t(as.matrix(data)), 1),cex=1,pos=3) 
