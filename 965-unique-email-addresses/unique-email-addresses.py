class Solution(object):
    def numUniqueEmails(self, emails):
        st  =set()

        for e in emails:

            name, domain = e.split("@")

            name = name.split("+")[0]
            name = name.replace(".","")

            st.add(name + "@" + domain)

        return len(st)        